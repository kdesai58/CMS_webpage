import hashlib
import os
from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from typing import List

from app.services.text_extraction import extract_text_from_pdf
from app.services.embeddings import generate_embeddings
from app.services.faiss_search import add_to_index
from app.db import save_file_metadata, is_file_duplicate

router = APIRouter()

@router.post("/")
async def upload_file(files: List[UploadFile] = File(...)):
    response = []

    # Ensure the uploads directory exists
    os.makedirs("uploads", exist_ok=True)

    for file in files:
        print(f"Received file: {file.filename}, content type: {file.content_type}")
        
        file_path = f"uploads/{file.filename}"
        print(f"Saving file to {file_path}...")
        
        # Generate the file hash
        file_content = await file.read()  # Read the content for hashing
        file_hash = hashlib.sha256(file_content).hexdigest()  # Generate hash
        await file.seek(0)  # Reset the file pointer so the content can be re-read

        # Check if the file is a duplicate
        if is_file_duplicate(file_hash):
            raise HTTPException(status_code=400, detail=f"File {file.filename} already exists in the database.")
    
        
        with open(file_path, "wb") as f:
            f.write(file_content)


        text = extract_text_from_pdf(file_path)
        embedding = generate_embeddings(text)
        # return {'embedding_id': embedding_id}
        doc_id = save_file_metadata(file.filename, text, file_hash)
        add_to_index(doc_id, embedding)

        response.append({
            "filename": file.filename,
            "message": "File uploaded and processed",
            "doc_id": doc_id,
            "text": text
        })

    return {"files": response}

@router.get("/")
def root():
    return {"message": "Hi, Welcome to upload page!"}