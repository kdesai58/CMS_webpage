# importing the required libraries
import hashlib
import os
from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from typing import List

# importing the required functions from the services and db modules
from app.services.text_extraction import extract_text_from_pdf
from app.services.embeddings import generate_embeddings
from app.services.faiss_search import add_to_index
from app.db import save_file_metadata, is_file_duplicate

# creating an instance of the APIRouter
router = APIRouter()

# endpoint to upload the multiple pdf files for processing via post request
@router.post("/")
async def upload_file(files: List[UploadFile] = File(...)):

    # Initialize the response list
    response = []

    # Ensure the uploads directory exists
    os.makedirs("uploads", exist_ok=True)

    # Iterate over the uploaded files
    for file in files:
        
        file_path = f"uploads/{file.filename}"
        
        # Generate the file hash
        file_content = await file.read()  # Read the content for hashing
        file_hash = hashlib.sha256(file_content).hexdigest()  # Generate hash
        await file.seek(0)  # Reset the file pointer so the content can be re-read

        # Check if the file is a duplicate
        if is_file_duplicate(file_hash):
            raise HTTPException(status_code=400, detail=f"File {file.filename} already exists in the database.")
    
        with open(file_path, "wb") as f:
            f.write(file_content)

        text = extract_text_from_pdf(file_path)   # Extract text from the pdf file
        embedding = generate_embeddings(text)  # Generate embeddings
        doc_id = save_file_metadata(file.filename, text, file_hash)  # Save metadata to the database
        add_to_index(doc_id, embedding)  # Add the document to the FAISS index

        # Append the response
        response.append({
            "filename": file.filename,
            "message": "File uploaded and processed",
        })

    return {"files": response}

# get request to root
@router.get("/")
def root():
    return {"message": "Hi, Welcome to upload page!"}