from fastapi import APIRouter, HTTPException

from app.services.embeddings import generate_embeddings
from app.services.faiss_search import search_embeddings
from app.db import get_metadata_by_id

router = APIRouter()

@router.post("/")
def search_documents(query: str, top_k: int = 3):
    query_embedding = generate_embeddings(query)
    # return {"shape": query_embedding.shape}
    distances, indices = search_embeddings(query_embedding, top_k)
    # x = indices.tolist()[0]
    results = [get_metadata_by_id(idx+1) for idx in indices if idx != -1]
    
    if not results:
        raise HTTPException(status_code=404, detail="No matching documents found")
    
    return {"query": query, "results": results}