from fastapi import APIRouter

from app.services.summarizer import generate_summary

router = APIRouter()

@router.post("/")
def summarize_pdf(text: str):
    summary = generate_summary(text)
    return {"summary": summary}