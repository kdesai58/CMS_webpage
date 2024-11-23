from fastapi import APIRouter

from app.services.classification import classify_document

router = APIRouter()

@router.post("/")
def classify(text: str, categories: list[str]):
    prediction = classify_document(text, categories)
    return {"text": text, "prediction": prediction}