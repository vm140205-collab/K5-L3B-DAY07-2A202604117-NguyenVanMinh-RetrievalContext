"""Connect to the Day 6 Qdrant embedded store (strategy C index, unchanged).

The store, chunk IDs, embedding model and dimensions are reused verbatim from
Day 6 (see day6/ manifest). This module only reads: scroll chunks for lexical
retrieval and query the dense index with a compatible query embedding.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from qdrant_client import QdrantClient, models

REPO_ROOT = Path(__file__).resolve().parents[2]
QDRANT_PATH = REPO_ROOT / "day6" / "qdrant_data"
COLLECTION = "day6_chunks"
STRATEGY = "C"  # best Day 6 configuration: paragraph 1200, page-scoped
FILTER_FIELDS = ("year", "primary_category", "document_type", "language")


class Day6Store:
    """Read-only adapter over the copied Day 6 embedded Qdrant collection."""

    def __init__(self, strategy: str = STRATEGY):
        self.strategy = strategy
        self.client = QdrantClient(path=str(QDRANT_PATH))
        info = self.client.get_collection(COLLECTION)
        self.dimensions = info.config.params.vectors.size
        self.strategy_count = self.count()

    def count(self) -> int:
        return self.client.count(
            COLLECTION,
            count_filter=models.Filter(must=[
                models.FieldCondition(key="strategy", match=models.MatchValue(value=self.strategy))]),
            exact=True).count

    def scroll_chunks(self) -> list[dict[str, Any]]:
        """All chunks of this strategy, with full payload (for BM25 index)."""
        records: list[dict[str, Any]] = []
        offset = None
        while True:
            batch, offset = self.client.scroll(
                collection_name=COLLECTION,
                scroll_filter=models.Filter(must=[
                    models.FieldCondition(key="strategy", match=models.MatchValue(value=self.strategy))]),
                limit=512, offset=offset, with_payload=True, with_vectors=False)
            records.extend(r.payload for r in batch)
            if offset is None:
                break
        return records

    def _filter(self, filters: dict[str, Any] | None) -> models.Filter:
        must = [models.FieldCondition(key="strategy", match=models.MatchValue(value=self.strategy))]
        for key, value in (filters or {}).items():
            if key not in FILTER_FIELDS:
                raise ValueError(f"unsupported filter field '{key}'; allowed: {FILTER_FIELDS}")
            must.append(models.FieldCondition(key=key, match=models.MatchValue(value=value)))
        return models.Filter(must=must)

    def dense_search(self, query_vector: list[float], top_k: int = 3,
                     filters: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        """Cosine top-k inside the Day 6 strategy, optionally restricted by metadata."""
        response = self.client.query_points(
            collection_name=COLLECTION, query=query_vector,
            query_filter=self._filter(filters), limit=top_k, with_payload=True)
        return [_to_result(rank, p.score, p.payload) for rank, p in enumerate(response.points, 1)]

    def fetch(self, chunk_ids: list[str]) -> list[dict[str, Any]]:
        """Fetch chunks by chunk_id (used to verify citation targets exist)."""
        response = self.client.scroll(
            collection_name=COLLECTION,
            scroll_filter=models.Filter(must=[
                models.FieldCondition(key="strategy", match=models.MatchValue(value=self.strategy)),
                models.FieldCondition(key="chunk_id", match=models.MatchAny(any=list(chunk_ids)))]),
            limit=len(chunk_ids) or 1, with_payload=True, with_vectors=False)
        return [r.payload for r in response[0]]


def _to_result(rank: int, score: float, payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": payload.get("chunk_id"),
        "chunk_id": payload.get("chunk_id"),
        "document_id": payload.get("document_id"),
        "source_id": payload.get("document_id"),
        "page": payload.get("page"),
        "section": payload.get("section"),
        "year": payload.get("year"),
        "primary_category": payload.get("primary_category"),
        "source": payload.get("source"),
        "text": payload.get("text", ""),
        "metadata": {k: v for k, v in payload.items()
                     if k not in ("chunk_id", "document_id", "page", "text", "strategy")},
        "score": round(float(score), 6),
        "rank": rank,
    }
