# importing required libraries
import faiss
import os
import numpy as np

# defining the index file name
INDEX_FILE = "vector_index.faiss"

# defining the dimension of the embeddings
dimention = 384
index = faiss.IndexFlatL2(dimention)  # L2 distance metric

# function to save the faiss index
def save_faiss_index():
    faiss.write_index(index, INDEX_FILE)
    print("FAISS index saved.")

# function to initialize the faiss index
def initialize_faiss_index():
    global index
    if os.path.exists(INDEX_FILE):  # Check if index file exists
        try:
            index = faiss.read_index(INDEX_FILE)  # Load the index
            print("FAISS index loaded successfully.")
        except Exception as e:
            print(f"Error loading FAISS index: {e}")
            index = faiss.IndexFlatL2(dimention)  # Reinitialize the index if loading fails
            print("Initialized a new FAISS index after failure.")
    else:
        index = faiss.IndexFlatL2(dimention)  # L2 distance metric
        print("Initialized a new FAISS index.")

initialize_faiss_index()   # Initialize the FAISS index

# function to add the embeddings to the index
def add_to_index(doc_id, embedding):
    index.add(np.array([embedding], dtype=np.float32))  # Add the embedding to the index
    save_faiss_index()
    return embedding

# function to search the embeddings
def search_embeddings(query_embedding, top_k):
    distances, indices = index.search(np.array([query_embedding], dtype=np.float32), top_k)
    return distances, indices