from fastapi import APIRouter
from api.v1.routes import books

api_router = APIRouter()

# ✅ Add root route for `/api/v1/`
@api_router.get("/")
def read_api():
    return {"message": "API v1 is working!"}

api_router.include_router(books.router, prefix="/books", tags=["books"])

