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
    
    # Debugging output
    print("Distances:", distances)
    print("Indices:", indices)

    results = []
    if len(indices) > 0:
        for idx in indices[0]:
            if idx > 0:  # Ensure valid index
                print("idx is ", idx)

                metadata = get_metadata_by_id(int(idx))  # FAISS indices start from 0
                print("metadata exicuted")
                # print(f"metadata is {metadata[1]}")
                # results.append({metadata[1]})
                # print("done")
                if metadata:
                    print("enter")
                    results.append({"id": metadata[0], "filename": metadata[1], "text": metadata[2]})
                    
    if not results:
        # Debugging: If results are empty, explain why
        print("No matching documents found. Indices:", indices, "Distances:", distances)
        raise HTTPException(status_code=404, detail="No matching documents found")
        
    return {"query": query, "results": results}

@router.get("/")
def root():
    return {"message": "Hi, Welcome to search page!"}