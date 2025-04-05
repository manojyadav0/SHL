import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load SentenceTransformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load SHL data
with open("backend/shl_data.json", "r") as f:
    data = json.load(f)

# Sanity check
print("Number of records in shl_data.json:", len(data))

# Handle case where description might be missing
texts = [f"{a['name']} {a.get('description', '')}" for a in data]

# Create embeddings
embeddings = model.encode(texts)

# Sanity check
print("Embedding shape:", embeddings.shape)

# FAISS Index
index = faiss.IndexFlatL2(embeddings[0].shape[0])
index.add(np.array(embeddings))

# Recommendation function
def recommend(query, top_k=10):
    query_vec = model.encode([query])
    D, I = index.search(query_vec, top_k)
    results = [data[i] for i in I[0]]
    return results

# Optional: test the function
if __name__ == "__main__":
    print("Testing Recommendation Engine...")
    sample_query = "logical reasoning test for freshers"
    recommendations = recommend(sample_query)
    for i, r in enumerate(recommendations):
        print(f"{i+1}. {r['name']}")
/usr/local/bin/python3 backend/embeddinngs.py
