from fastapi import APIRouter, File, UploadFile, Form

from services.text_extraction import extract_text_from_pdf
from services.embeddings import generate_embeddings
from services.faiss_search import add_to_index
from db import save_file_metadata

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    text = extract_text_from_pdf(file_path)
    embedding = generate_embeddings(text)
    add_to_index(embedding)
    save_file_metadata(file.filename, text, embedding, [])

    return {"filename": file.filename, "message": "File uploaded and processed"}