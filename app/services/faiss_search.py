import faiss
import os
import numpy as np

INDEX_FILE = "vector_index.faiss"

dimention = 384
index = faiss.IndexFlatL2(dimention)

def save_faiss_index():
    faiss.write_index(index, INDEX_FILE)
    print("FAISS index saved.")

# Initialize or load FAISS index
def initialize_faiss_index():
    global index
    if faiss.read_index(INDEX_FILE):
        index = faiss.read_index(INDEX_FILE)
        print("FAISS index loaded.")
    else:
        index = faiss.IndexFlatL2(dimention)  # L2 distance metric
        print("Initialized a new FAISS index.")

initialize_faiss_index()

def add_to_index(doc_id, embedding):
    index.add(np.array([embedding], dtype=np.float32))
    save_faiss_index()
    return embedding

def search_embeddings(query_embedding, top_k):
    distances, indices = index.search(np.array([query_embedding], dtype=np.float32), top_k)
    return distances, indices