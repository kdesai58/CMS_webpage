from fastapi import APIRouter, UploadFile, File
from typing import List

router = APIRouter()

@router.post("/summarize/")
async def summarize_pdf(files: List[UploadFile] = File(...)):
    summaries = []
    for file in files:
        # Simulated summarization process
        content = await file.read()
        summary = f"Summary for {file.filename}: {len(content)} bytes processed."
        summaries.append({"filename": file.filename, "summary": summary})

    return {"summaries": summaries}
