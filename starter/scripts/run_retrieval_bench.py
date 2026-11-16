"""Retrieval benchmark: run one or more methods on a split, report comparable metrics.

Metrics (BENCHMARK.md definitions, identical hit rule and cutoff for all runs):
- Hit@1:               answerable questions with valid evidence in top-1 / N
- Evidence Hit@3:      answerable questions with valid evidence in top-3 / N
- Context Evidence Rate: answerable questions whose final packed context
                       (top-k, budget) contains valid evidence / N
A hit = chunk from the gold source, on a gold page, containing the evidence
quote (whitespace-insensitive). Unanswerable questions are excluded from all
denominators. Gold never enters any query or filter.

Usage:
  python starter/scripts/run_retrieval_bench.py --method dense --split dev \
      --top-k 3 --budget 800 --output results/retrieval/dense-dev
"""
import argparse
import json
import re
import statistics
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from embedder import QueryEmbedder  # noqa: E402
from retrieval import Bm25Retriever, DenseRetriever, HybridRrfRetriever  # noqa: E402
from store import Day6Store  # noqa: E402


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def is_hit(chunk: dict, gold: list[dict]) -> bool:
    return any(chunk["source_id"] == g["source_id"] and chunk["page"] == g["page"]
               and squash(g["evidence"]) in squash(chunk["text"]) for g in gold)


def pack_context(results: list[dict], budget: int) -> tuple[str, list[str]]:
    """Same packing rule as the starter baseline: dedup by id, cumulative budget."""
    blocks, ids, seen = [], [], set()
    for c in results:
        if c["id"] in seen:
            continue
        seen.add(c["id"])
        block = f"[{c['id']} | {c['source']} | page {c['page']}]\n{c['text']}"
        if len("\n\n".join(blocks + [block])) <= budget:
            blocks.append(block)
            ids.append(c["id"])
    return "\n\n".join(blocks), ids


def main() -> None:
    parser = argparse.ArgumentParser(description="Retrieval benchmark cho Day 7")
    parser.add_argument("--method", required=True, choices=("dense", "bm25", "hybrid_rrf"))
    parser.add_argument("--split", required=True, choices=("dev", "test"))
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--budget", type=int, default=800)
    parser.add_argument("--retrieval-k", type=int, default=None,
                        help="candidates fetched before cutting to top-k (hybrid pool)")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    questions = [json.loads(l) for l in
                 (REPO_ROOT / "benchmark" / "questions.jsonl").read_text(encoding="utf-8").splitlines()]
    selected = [q for q in questions if q["split"] == args.split]
    answerable = [q for q in selected if q["answerable"]]
    if not answerable:
        raise SystemExit("không có câu có đáp án trong split")

    store = Day6Store()
    embedder = QueryEmbedder()
    chunks = store.scroll_chunks()
    if args.method == "dense":
        retriever = DenseRetriever(store, embedder)
    elif args.method == "bm25":
        retriever = Bm25Retriever(chunks)
    else:
        retriever = HybridRrfRetriever(DenseRetriever(store, embedder), Bm25Retriever(chunks))

    traces = []
    for q in selected:
        filters = None  # no gold-derived filters; metadata filters are agent-side only
        started = time.perf_counter()
        if args.retrieval_k and args.method == "hybrid_rrf":
            # fuse a wider pool, then keep the first top-k for ranking comparison
            results = retriever.search(q["question"], top_k=args.retrieval_k)[:args.top_k]
            for i, h in enumerate(results, 1):
                h["rank"] = i
        else:
            results = retriever.search(q["question"], top_k=args.top_k)
        elapsed_ms = (time.perf_counter() - started) * 1000
        context, context_ids = pack_context(results, args.budget)
        marked = [{**c, "hit": is_hit(c, q["gold"])} for c in results] if q["answerable"] else \
                 [{**c, "hit": None} for c in results]
        traces.append({
            "query_id": q["id"], "split": q["split"], "answerable": q["answerable"],
            "question": q["question"], "method": args.method, "top_k": args.top_k,
            "budget_chars": args.budget, "results": marked, "context": context,
            "context_ids": context_ids, "context_chars": len(context),
            "elapsed_ms": round(elapsed_ms, 1),
            "hit1": bool(q["answerable"] and marked and marked[0]["hit"]),
            "hit3": bool(q["answerable"] and any(c["hit"] for c in marked)),
            "context_hit": bool(q["answerable"] and any(
                c["hit"] and c["id"] in context_ids for c in marked)),
        })

    answerable_traces = [t for t in traces if t["answerable"]]
    n = len(answerable_traces)
    summary = {
        "method": args.method, "split": args.split, "top_k": args.top_k,
        "budget_chars": args.budget, "n_answerable": n,
        "hit1": f"{sum(t['hit1'] for t in answerable_traces)}/{n}",
        "hit1_rate": round(sum(t["hit1"] for t in answerable_traces) / n, 4),
        "evidence_hit3": f"{sum(t['hit3'] for t in answerable_traces)}/{n}",
        "evidence_hit3_rate": round(sum(t["hit3"] for t in answerable_traces) / n, 4),
        "context_evidence_rate": f"{sum(t['context_hit'] for t in answerable_traces)}/{n}",
        "context_evidence_rate_pct": round(sum(t["context_hit"] for t in answerable_traces) / n, 4),
        "avg_context_chars": round(statistics.mean(t["context_chars"] for t in traces), 1),
        "median_ms": round(statistics.median(t["elapsed_ms"] for t in traces), 1),
        "service_cost_usd": 0.0,
    }
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "traces.json").write_text(
        json.dumps(traces, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.output / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
