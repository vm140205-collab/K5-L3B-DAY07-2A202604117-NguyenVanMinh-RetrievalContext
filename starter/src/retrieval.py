"""Three retrieval methods over the same Day 6 corpus / chunk IDs / index.

1. Dense retrieval  — query embedding + cosine search in the Day 6 Qdrant store.
2. Lexical retrieval — BM25 over the same strategy-C chunks (English corpus,
   simple word tokenizer; note: a Vietnamese corpus would need a syllable-
  /word-level tokenizer, recorded as a limitation for such corpora).
3. Hybrid retrieval — Reciprocal Rank Fusion of the two rankings (RRF k=60).

All three return the same result schema (id/text/source_id/source/page/
metadata/score/rank) so they are directly comparable on identical questions.
"""
from __future__ import annotations

import re
import time
import unicodedata
from typing import Any

from rank_bm25 import BM25Okapi

from embedder import QueryEmbedder
from store import Day6Store

RRF_K = 60


def tokenize(text: str) -> list[str]:
    """Simple word tokenizer for the English corpus (casefold + NFC)."""
    return re.findall(r"\w+", unicodedata.normalize("NFC", text).casefold())


class DenseRetriever:
    """Method 1: query embedding + cosine search in the Day 6 vector store."""

    name = "dense"

    def __init__(self, store: Day6Store, embedder: QueryEmbedder):
        self.store = store
        self.embedder = embedder

    def search(self, query: str, *, top_k: int = 3,
               filters: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        vector = self.embedder.embed_query(query)
        results = self.store.dense_search(vector, top_k=top_k, filters=filters)
        for r in results:
            r["method"] = self.name
        return results


class Bm25Retriever:
    """Method 2: BM25 lexical ranking over the same chunks (no vectors)."""

    name = "bm25"

    def __init__(self, chunks: list[dict[str, Any]]):
        self.chunks = chunks
        self.ids = [c["chunk_id"] for c in chunks]
        corpus_tokens = [tokenize(c["text"]) for c in chunks]
        self.index = BM25Okapi(corpus_tokens)

    def search(self, query: str, *, top_k: int = 3,
               filters: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        if filters:
            raise ValueError("BM25 retriever does not support metadata filters")
        scores = self.index.get_scores(tokenize(query))
        ranked = sorted(range(len(scores)), key=lambda i: (-scores[i], self.ids[i]))[:top_k]
        results = []
        for rank, i in enumerate(ranked, 1):
            if scores[i] <= 0:
                break
            payload = self.chunks[i]
            results.append({
                "id": payload["chunk_id"], "chunk_id": payload["chunk_id"],
                "document_id": payload["document_id"], "source_id": payload["document_id"],
                "page": payload["page"], "section": payload.get("section"),
                "year": payload.get("year"), "primary_category": payload.get("primary_category"),
                "source": payload.get("source", ""), "text": payload["text"],
                "metadata": {k: v for k, v in payload.items()
                            if k not in ("chunk_id", "document_id", "page", "text", "strategy")},
                "score": round(float(scores[i]), 6), "rank": rank, "method": self.name,
            })
        return results


class HybridRrfRetriever:
    """Method 3: Reciprocal Rank Fusion of dense + BM25 rankings.

    score(d) = sum over methods of 1 / (RRF_K + rank_method(d)).
    RRF needs no score normalization, which is why it is preferred here over
    raw score fusion of cosine and BM25 scales.
    """

    name = "hybrid_rrf"

    def __init__(self, dense: DenseRetriever, bm25: Bm25Retriever, rrf_k: int = RRF_K):
        self.dense = dense
        self.bm25 = bm25
        self.rrf_k = rrf_k

    def search(self, query: str, *, top_k: int = 3,
               filters: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        pool_k = max(top_k, 10)  # fuse a wider pool, then cut to top_k
        dense_hits = self.dense.search(query, top_k=pool_k, filters=filters)
        bm25_hits = self.bm25.search(query, top_k=pool_k) if not filters else []
        fused: dict[str, dict[str, Any]] = {}
        scores: dict[str, float] = {}
        for hits in (dense_hits, bm25_hits):
            for h in hits:
                cid = h["id"]
                fused.setdefault(cid, h)
                scores[cid] = scores.get(cid, 0.0) + 1.0 / (self.rrf_k + h["rank"])
        ranked = sorted(scores, key=lambda cid: (-scores[cid], cid))[:top_k]
        results = []
        for rank, cid in enumerate(ranked, 1):
            h = dict(fused[cid])
            h["score"] = round(scores[cid], 6)
            h["rank"] = rank
            h["method"] = self.name
            results.append(h)
        return results


def timed_search(retriever, query: str, *, top_k: int = 3,
                 filters: dict[str, Any] | None = None) -> tuple[list[dict[str, Any]], float]:
    started = time.perf_counter()
    results = retriever.search(query, top_k=top_k, filters=filters)
    return results, (time.perf_counter() - started) * 1000
