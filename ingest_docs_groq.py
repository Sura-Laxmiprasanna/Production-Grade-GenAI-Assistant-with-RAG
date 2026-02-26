# backend/scripts/ingest_docs_groq.py
import json
import numpy as np

# Load docs.json
with open("data/docs.json", "r") as f:  # ✅ read mode
    docs = json.load(f)

vector_store = []

for doc in docs:
    # Simple chunking by sentence
    chunks = doc['content'].split(". ")
    for i, chunk in enumerate(chunks):
        vector_store.append({
            "id": doc['id'],
            "title": doc['title'],
            "chunk_index": i,
            "content": chunk,
            "vector": np.random.rand(1536).tolist()  # mock embeddings
        })

# Save vector store
with open("data/vector_store.json", "w") as f:  # ✅ write mode
    json.dump(vector_store, f, indent=2)

print("✅ Created vector_store.json with mock embeddings")