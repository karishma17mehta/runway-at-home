import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.rag_module import retrieve_context

def test_retrieve_context():
    results = retrieve_context("gothcore", top_k=3)
    assert isinstance(results, list)
    assert len(results) > 0
    assert "trend_name" in results[0]
    assert "description" in results[0]

if __name__ == "__main__":
    test_retrieve_context()
    print("✅ RAG test passed")