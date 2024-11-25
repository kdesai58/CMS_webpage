import faiss
import os
import numpy as np

INDEX_FILE = "vector_index.faiss"

dimention = 384
index = faiss.IndexFlatL2(dimention)

def save_faiss_index():
    faiss.write_index(index, "vector_index.faiss")

def load_faiss_index(dimension=384):
    global index
    if os.path.exists(INDEX_FILE):
        index = faiss.read_index(INDEX_FILE)
        print(f"FAISS index loaded from {INDEX_FILE}")
    else:
        index = faiss.IndexFlatL2(dimension)
        print("Initialized new FAISS index")

def add_to_index(embedding):
    index.add(np.array([embedding], dtype=np.float32))
    save_faiss_index()
    return index.ntotal-1

def search_embeddings(query_embedding, top_k):
    distances, indices = index.search(np.array([query_embedding], dtype=np.float32), top_k)
    return distances[0], indices[0]