import faiss
import os
import numpy as np

INDEX_FILE = "vector_index.faiss"

dimention = 384
index = faiss.IndexFlatL2(dimention)

def save_faiss_index():
    faiss.write_index(index, INDEX_FILE)
    print("FAISS index saved.")

def initialize_faiss_index():
    global index
    if os.path.exists(INDEX_FILE):  # Check if index file exists
        try:
            index = faiss.read_index(INDEX_FILE)
            print("FAISS index loaded successfully.")
        except Exception as e:
            print(f"Error loading FAISS index: {e}")
            # Reinitialize the index if loading fails
            index = faiss.IndexFlatL2(dimention)
            print("Initialized a new FAISS index after failure.")
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