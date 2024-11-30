# importing required libraries
from fastapi import APIRouter, HTTPException

# importing required functions
from app.services.embeddings import generate_embeddings
from app.services.faiss_search import search_embeddings
from app.db import get_metadata_by_id

# creating an instance of APIRouter
router = APIRouter()

# endpoint to search the documents via get request
@router.get("/")
def search_documents(query: str, top_k: int = 3):

    query_embedding = generate_embeddings(query)   # Generate embeddings for the query
    distances, indices = search_embeddings(query_embedding, top_k)   # Search for similar embeddings and getting distances and indices
    
    # Debugging output
    print("Distances:", distances)
    print("Indices:", indices)

    # from indices, get metadata from cms database and store the id and filename in results
    results = []
    if len(indices) > 0:
        for idx in indices[0]:
            if idx > -1:  # Ensure valid index
                
                print("idx is ", (idx+1))
                metadata = get_metadata_by_id(int(idx+1))  # FAISS indices start from 0
                print("metadata exicuted")
                if metadata:  # Ensure valid metadata 
                    results.append({"id": metadata[0], "filename": metadata[1]})

    # If no results found, raise an exception      
    if not results:
        print("No matching documents found. Indices:", indices, "Distances:", distances)
        raise HTTPException(status_code=404, detail="No matching documents found")
        
    return {"query": query, "results": results}

# get request to root
@router.get("/")
def root():
    return {"message": "Hi, Welcome to search page!"}