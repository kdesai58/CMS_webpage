from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.search import router as search_router
from app.routes.classify import router as classify_router


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(upload_router, prefix="/upload", tags=["upload"])
app.include_router(search_router, prefix="/search", tags=["search"])
app.include_router(classify_router, prefix="/classify", tags=["classify"])

@app.get("/")
def root():
    return {"message": "Hi, Welcome to Content Management System!"}
    