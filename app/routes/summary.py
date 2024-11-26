from fastapi import APIRouter, UploadFile

from app.services.summarizer import generate_summary

router = APIRouter()

@router.post("/summarize/")
async def summarize_pdf(files: List[UploadFile] = File(...)):
    summaries = []
    for file in files:
        summary = generate_summary(text)

    return {"summaries": summaries}
