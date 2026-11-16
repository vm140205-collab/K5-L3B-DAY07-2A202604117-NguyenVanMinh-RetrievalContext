"""Smoke test: open the Day 6 store, embed a query, run a dense search."""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from store import Day6Store  # noqa: E402
from embedder import QueryEmbedder  # noqa: E402


def main() -> None:
    t0 = time.time()
    store = Day6Store()
    print(f"store open: {time.time() - t0:.1f}s, dim={store.dimensions}, "
          f"strategy C chunks: {store.strategy_count}")

    t0 = time.time()
    emb = QueryEmbedder()
    print(f"embedder load: {emb.load_seconds}s (total {time.time() - t0:.1f}s incl. model download)")

    t0 = time.time()
    qvec = emb.embed_query("What does the paper propose instead of looking backwards?")
    hits = store.dense_search(qvec, top_k=3)
    print(f"query: {time.time() - t0:.2f}s")
    for h in hits:
        print(f"  {h['rank']}. {h['chunk_id']} {h['document_id']} p{h['page']} score={h['score']}")
        print(f"     {h['text'][:140]!r}")


if __name__ == "__main__":
    main()
