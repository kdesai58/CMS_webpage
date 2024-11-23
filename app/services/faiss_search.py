import faiss
import numpy as np

dimention = 768
index = faiss.IndexFlatL2(dimention)

def add_to_index(embedding):
    index.add(np.array([embedding], dtype=np.float32))

def search_embeddings(query_embedding, top_k):
    distances, indices = index.search(np.array([query_embedding], dtype=np.float32), top_k)
    return distances, indices