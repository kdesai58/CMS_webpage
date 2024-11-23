from fastapi import APIRouter, HTTPException

from app.services.embeddings import generate_embeddings
from app.services.faiss_search import search_embeddings
from app.db import get_file_by_index

router = APIRouter()

@router.post("/")
def search_documents(query: str, top_k: int = 3):
    query_embedding = generate_embeddings(query)
    distances, indices = search_embeddings(query_embedding, top_k)
    results = [get_file_by_index(index) for index in indices[0]]
    
    if not results:
        raise HTTPException(status_code=404, detail="No matching documents found")
    
    return {"query": query, "results": results}