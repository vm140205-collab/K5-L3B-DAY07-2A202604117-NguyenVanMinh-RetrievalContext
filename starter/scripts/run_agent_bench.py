"""Run the configured agent over one split; write traces + cases for review.

Configs are named presets (see CONFIGS below) so every run is reproducible.
Per-question usage is the delta of the shared client's token counters.

Usage:
  python starter/scripts/run_agent_bench.py --config dense800 --split dev \
      --output results/agent/dense800-dev
"""
import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from agent import Agent, MistralClient  # noqa: E402
from embedder import QueryEmbedder  # noqa: E402
from retrieval import Bm25Retriever, DenseRetriever, HybridRrfRetriever  # noqa: E402
from store import Day6Store  # noqa: E402

# Named agent configurations. tools = retrieval tools exposed to the model.
CONFIGS = {
    # Baseline: dense-only, starter-default budget (too small for the chunks).
    "dense800": {"tools": ["search_dense"], "top_k": 3, "budget": 800,
                 "max_tool_calls": 2, "max_turns": 6},
    # Improvement 1: hybrid tool + budget that fits whole chunks.
    "hybrid3500": {"tools": ["search_hybrid"], "top_k": 3, "budget": 3500,
                   "max_tool_calls": 2, "max_turns": 6},
    # Improvement 2: all three tools, more searches, wider top-k.
    "alltools": {"tools": ["search_dense", "search_bm25", "search_hybrid"],
                 "top_k": 5, "budget": 3500, "max_tool_calls": 4, "max_turns": 10},
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Chạy agent trên một split")
    parser.add_argument("--config", required=True, choices=sorted(CONFIGS))
    parser.add_argument("--split", required=True, choices=("dev", "test"))
    parser.add_argument("--model", default="mistral-small-latest")
    parser.add_argument("--reasoning-effort", default=None,
                        choices=("none", "low", "medium", "high"))
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    cfg = CONFIGS[args.config]

    questions = [json.loads(l) for l in
                 (REPO_ROOT / "benchmark" / "questions.jsonl").read_text(encoding="utf-8").splitlines()]
    selected = [q for q in questions if q["split"] == args.split]

    store = Day6Store()
    embedder = QueryEmbedder()
    chunks = store.scroll_chunks()
    retrievers = {
        "search_dense": DenseRetriever(store, embedder),
        "search_bm25": Bm25Retriever(chunks),
        "search_hybrid": HybridRrfRetriever(DenseRetriever(store, embedder),
                                            Bm25Retriever(chunks)),
    }
    client = MistralClient(model=args.model, reasoning_effort=args.reasoning_effort)
    agent = Agent(client, retrievers, cfg["tools"], top_k=cfg["top_k"],
                  budget=cfg["budget"], max_tool_calls=cfg["max_tool_calls"],
                  max_turns=cfg["max_turns"])

    # Idempotent resume: if the output dir already has a partial traces.jsonl
    # (e.g. a previous run was aborted mid-way), reuse those results and only
    # run the questions that are missing. Delete traces.jsonl to force a full
    # rerun.
    traces: list[dict] = []
    done_ids: set[str] = set()
    prior = args.output / "traces.jsonl"
    if prior.exists():
        traces = [json.loads(l) for l in prior.read_text(encoding="utf-8").splitlines()]
        # Only completed answers are reused; provider errors are retried.
        traces = [t for t in traces if t.get("status") != "error"]
        done_ids = {t["query_id"] for t in traces}
        print(f"resume: {len(done_ids)} completed questions reused from {prior}; "
              f"running the remaining {sum(1 for q in selected if q['id'] not in done_ids)}")

    cases = []
    for q in selected:
        if q["id"] in done_ids:
            cases.append({"id": q["id"], "split": q["split"], "answerable": q["answerable"]})
            continue
        before = dict(client.usage)
        try:
            result = agent.run(q["question"])
            result["query_id"] = q["id"]
            result["question"] = q["question"]
            result["answerable"] = q["answerable"]
            result["expected_answer"] = q["expected_answer"] if q["answerable"] else None
            result["gold"] = q.get("gold")
            result["usage_delta"] = {k: client.usage[k] - before.get(k, 0)
                                     for k in ("prompt_tokens", "completion_tokens",
                                               "total_tokens", "calls")}
            traces.append(result)
        except Exception as exc:  # provider/store errors are recorded, never faked
            traces.append({"query_id": q["id"], "question": q["question"],
                           "answerable": q["answerable"], "status": "error",
                           "error": f"{type(exc).__name__}: {exc}",
                           "events": [], "citations": []})
        cases.append({"id": q["id"], "split": q["split"], "answerable": q["answerable"]})
        print(f"{q['id']}: {traces[-1]['status']} "
              f"({traces[-1].get('n_tool_calls', 0)} tool calls)", flush=True)

    cost = client.cost_usd()
    summary = {
        "config": args.config, "split": args.split, "model": args.model,
        "reasoning_effort": args.reasoning_effort,
        "cfg": cfg, "n": len(traces),
        "status_counts": {s: sum(1 for t in traces if t["status"] == s)
                          for s in ("answered", "abstain", "error")},
        "usage": dict(client.usage),
        "cost_usd": round(cost, 6) if cost is not None else None,
    }
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "traces.jsonl").write_text(
        "\n".join(json.dumps(t, ensure_ascii=False) for t in traces) + "\n", encoding="utf-8")
    # agent_metrics.py expects a JSON array; keep both formats.
    (args.output / "traces.json").write_text(
        json.dumps(traces, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.output / "cases.json").write_text(
        json.dumps(cases, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (args.output / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
