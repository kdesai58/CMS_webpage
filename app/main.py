from fastapi import FastAPI
from app.routes import upload, search, classify 

app = FastAPI()


app.include_router(upload.router, prefix="/upload", tags=["upload"])
app.include_router(search.router, prefix="/search", tags=["search"])
app.include_router(classify.router, prefix="/classify", tags=["classify"])

@app.get("/")
def root():
    return {"message": "Hi, Welcome to Content Management System!"}