# importing required libraries
import hashlib
from fastapi import APIRouter, UploadFile, File
from typing import List

# importing required functions from the services and db modules
from app.db import is_file_duplicate, save_file_metadata
from app.services.embeddings import generate_embeddings
from app.services.faiss_search import add_to_index
from app.services.summarizer import generate_summary
from app.services.text_extraction import extract_text_from_pdf

# creating an instance of the APIRouter
router = APIRouter()

# endpoint to summarize the multiple pdf files for processing via post request
@router.post("/summarize/")
async def summarize_pdf(files: List[UploadFile] = File(...)):
    
    # Initialize the summaries list
    summaries = []

    # Iterate over the uploaded files
    for file in files:
        file_path = f"uploads/{file.filename}"
        file_content = await file.read()

        file_hash = hashlib.sha256(file_content).hexdigest()  # Generate hash
        await file.seek(0)  # Reset the file pointer so the content can be re-read

        with open(file_path, "wb") as f:
            f.write(file_content)

        # if the file is a duplicate then just generate the summary
        if is_file_duplicate(file_hash):
            text = extract_text_from_pdf(file_path)
            summary = generate_summary(text)
            summaries.append({"filename": file.filename, "Status": f"{file.filename} is already in the database." , "summary": summary})
        # else process the file, add it to the database and generate the summary
        else:
            text = extract_text_from_pdf(file_path)
            summary = generate_summary(text)
            embedding = generate_embeddings(text)
            doc_id = save_file_metadata(file.filename, text, file_hash)
            add_to_index(doc_id, embedding)
            summaries.append({"filename": file.filename, "Status": f"{file.filename} is proccessed and added to the database." , "summary": summary})
            

    return {"summaries": summaries}

# get request to root
@router.get("/")
def root():
    return {"message": "Hi, Welcome to the summary page!"}
