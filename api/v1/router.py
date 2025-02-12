from fastapi import APIRouter

from api.v1.routes import books, stage2  # Import new route file

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])
api_router.include_router(stage2.router, prefix="/stage2", tags=["stage2"]) 

