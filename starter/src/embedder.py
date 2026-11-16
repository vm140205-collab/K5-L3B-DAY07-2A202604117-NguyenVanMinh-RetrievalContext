"""Query embeddings compatible with the Day 6 index: BAAI/bge-small-en-v1.5.

Same model, same 384 dimensions, same `query_embed` retrieval prefix as Day 6.
"""
from __future__ import annotations

import time

from fastembed import TextEmbedding

MODEL_NAME = "BAAI/bge-small-en-v1.5"
DIMENSIONS = 384


class QueryEmbedder:
    def __init__(self, model_name: str = MODEL_NAME):
        started = time.time()
        self.model_name = model_name
        self.dimensions = DIMENSIONS
        self._model = TextEmbedding(model_name=model_name)
        self.load_seconds = round(time.time() - started, 1)
        self.queries_embedded = 0

    def embed_query(self, question: str) -> list[float]:
        vector = [float(x) for x in next(iter(self._model.query_embed(question)))]
        if len(vector) != self.dimensions:
            raise RuntimeError(f"unexpected dimension {len(vector)} != {self.dimensions}")
        self.queries_embedded += 1
        return vector
