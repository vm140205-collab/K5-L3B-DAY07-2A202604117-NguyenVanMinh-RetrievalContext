"""Verify the unanswerable questions have no evidence in the corpus.

For each unanswerable question: (1) keyword scan over all pages (day6/pages.jsonl),
(2) dense + BM25 top-10 retrieval, printing what the corpus actually offers so a
human can confirm nothing supports the claim.
"""
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from embedder import QueryEmbedder  # noqa: E402
from retrieval import Bm25Retriever, DenseRetriever  # noqa: E402
from store import Day6Store  # noqa: E402

CHECKS = {
    "u01": ["partially observable", "POMDP", "polynomial-time algorithm"],
    "u02": ["Lipschitz constant", "contraction", "Q-learning"],
    "u03": ["GPU", "A100", "V100", "RTX", "graphics card"],
    "u04": ["quadruped", "ANYmal", "Spot robot", "robot dog"],
}


def main() -> None:
    pages = [json.loads(l) for l in
             (REPO_ROOT / "day6" / "pages.jsonl").read_text(encoding="utf-8").splitlines()]
    questions = [json.loads(l) for l in
                 (REPO_ROOT / "benchmark" / "questions.jsonl").read_text(encoding="utf-8").splitlines()]
    unanswerable = [q for q in questions if not q["answerable"]]

    store = Day6Store()
    chunks = store.scroll_chunks()
    dense = DenseRetriever(store, QueryEmbedder())
    bm25 = Bm25Retriever(chunks)

    for q in unanswerable:
        print(f"===== {q['id']} =====")
        print(f"Q: {q['question']}")
        for term in CHECKS[q["id"]]:
            hits = [(p["document_id"], p["page"]) for p in pages
                    if re.search(re.escape(term), p["text"], re.IGNORECASE)]
            print(f"  scan {term!r}: {len(hits)} pages -> {hits[:6]}")
        for method, retriever in (("dense", dense), ("bm25", bm25)):
            top = retriever.search(q["question"], top_k=10)
            print(f"  {method} top-10:")
            for h in top[:5]:
                print(f"    {h['score']:.4f} {h['document_id']} p{h['page']}: {h['text'][:90]!r}")
        print()


if __name__ == "__main__":
    main()
