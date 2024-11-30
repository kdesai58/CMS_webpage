# importing needed libraries and modules from app/routes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.upload import router as upload_router
from app.routes.search import router as search_router
from app.routes.summary import router as summary_router

# creating FastAPI instance
app = FastAPI()

# adding CORS middleware to allow requests from frontend
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

# including routers to the app
app.include_router(upload_router, prefix="/upload", tags=["upload"])
app.include_router(search_router, prefix="/search", tags=["search"])
app.include_router(summary_router, prefix="/summary", tags=["summary"])

# root route
@app.get("/")
def root():
    return {"message": "Hi, Welcome to Content Management System!"}
    