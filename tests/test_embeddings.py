import pytest
from src.embedding_engine import EmbeddingEngine

def test_embedding_encode():
    engine = EmbeddingEngine()
    texts = ["Hello world", "Test sentence"]
    emb = engine.encode(texts)
    assert emb.shape[0] == 2

import pytest
from src.embedding_engine import EmbeddingEngine

def test_embedding_encode():
    engine = EmbeddingEngine()
    texts = ["Hello world", "Test sentence"]
    emb = engine.encode(texts)
    assert emb.shape[0] == 2

