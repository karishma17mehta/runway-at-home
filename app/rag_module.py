import os
import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb

CSV_PATH = "/content/drive/MyDrive/RAT_project/data/trend_corpus_dataset.csv"
PERSIST_PATH = "/content/drive/MyDrive/RAT_project/data/chroma_db/"

# Load trend data
print("📄 Loading trend corpus...")
df = pd.read_csv(CSV_PATH)
descriptions = df["description"].tolist()
trend_names = df["trend_name"].tolist()

# Load embedding model
print("🧠 Loading sentence transformer model...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to or create Chroma vector DB
print("🔗 Connecting to Chroma DB at:", PERSIST_PATH)
client = chromadb.PersistentClient(path=PERSIST_PATH)
collection = client.get_or_create_collection(name="trends")

# Check if already populated
if collection.count() == 0:
    print("📤 Inserting vectors into ChromaDB for the first time...")
    vectors = embedder.encode(descriptions, convert_to_numpy=True).tolist()
    collection.add(
        documents=descriptions,
        metadatas=[{"trend_name": t} for t in trend_names],
        ids=[f"id_{i}" for i in range(len(descriptions))],
        embeddings=vectors
    )
    print("✅ Insertion complete.")
else:
    print(f"📁 Loaded existing Chroma collection with {collection.count()} items.")

# Retrieval function
def retrieve_context(query, top_k=3):
    print(f"🔍 Retrieving top {top_k} matches for: '{query}'")
    query_vec = embedder.encode([query])[0].tolist()
    results = collection.query(query_embeddings=[query_vec], n_results=top_k)
    
    return [
        {"trend_name": meta["trend_name"], "description": doc}
        for doc, meta in zip(results["documents"][0], results["metadatas"][0])
    ]