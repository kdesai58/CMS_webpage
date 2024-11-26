import hashlib
from typing import List
from fastapi import APIRouter, File, UploadFile

from app.db import is_file_duplicate, save_file_metadata
from app.services.embeddings import generate_embeddings
from app.services.faiss_search import add_to_index
from app.services.summarizer import generate_summary
from app.services.text_extraction import extract_text_from_pdf

router = APIRouter()

@router.post("/")
async def summarize_pdf(files: List[UploadFile] = File(...)):
    responce = []
    for file in files:
        file_path = f"uploads/{file.filename}"
        file_content = await file.read()

        file_hash = hashlib.sha256(file_content).hexdigest()  # Generate hash
        await file.seek(0)  # Reset the file pointer so the content can be re-read

        with open(file_path, "wb") as f:
            f.write(file_content)

        if is_file_duplicate(file_hash):
            text = extract_text_from_pdf(file_path)
            summary = generate_summary(text)
            responce.append({
                "filename": file.filename,
                "message": "File already exists in the database",
                "summary": summary
            })
        else:
            text = extract_text_from_pdf(file_path)
            embedding = generate_embeddings(text)
            # return {'embedding_id': embedding_id}
            doc_id = save_file_metadata(file.filename, text, file_hash)
            add_to_index(doc_id, embedding)
            summary = generate_summary(text)
            responce.append({
                "filename": file.filename,
                "message": "File uploaded and processed",
                "summary": summary
            })

    return {"summaries of files": responce}