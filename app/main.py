from fastapi import FastAPI, File
from app.routes.upload import router as upload_router
from app.routes.search import router as search_router
from app.routes.classify import router as classify_router


app = FastAPI()


app.include_router(upload_router, prefix="/upload", tags=["upload"])
app.include_router(search_router, prefix="/search", tags=["search"])
app.include_router(classify_router, prefix="/classify", tags=["classify"])

@app.get("/")
def root():
    return {"message": "Hi, Welcome to Content Management System!"}
    