from fastapi import APIRouter, File, UploadFile, Form

from app.services.text_extraction import extract_text_from_pdf
from app.services.embeddings import generate_embeddings
from app.services.faiss_search import add_to_index, save_faiss_index
from app.db import save_file_metadata

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)
    embedding = generate_embeddings(text)
    # return {'embedding_id': embedding_id}
    doc_id = save_file_metadata(file.filename, text)
    add_to_index(doc_id, embedding)

    return {"filename": file.filename, "message": "File uploaded and processed", "doc_id": doc_id, "text": text}

@router.get("/")
def root():
    return {"message": "Hi, Welcome to upload page!"}