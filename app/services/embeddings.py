from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(text):
    embeddings = model.encode(text)#.tolist()
    return embeddings