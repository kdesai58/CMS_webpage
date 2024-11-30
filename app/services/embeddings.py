# importing sentence_transformers from SentenceTransformer library
from sentence_transformers import SentenceTransformer

# loading the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# function to generate embeddings
def generate_embeddings(text):
    embeddings = model.encode([text])[0]
    return embeddings