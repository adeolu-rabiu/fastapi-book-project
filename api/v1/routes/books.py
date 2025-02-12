from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from api.db.schemas import Book, Genre, InMemoryDB  # Changed from api.v1.db.schemas to api.db.schemas

router = APIRouter()

db = InMemoryDB()
db.books = {
    1: Book(
        id=1,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        publication_year=1937,
        genre=Genre.SCI_FI,
    ),
    2: Book(
        id=2,
        title="The Lord of the Rings",
        author="J.R.R. Tolkien",
        publication_year=1954,
        genre=Genre.FANTASY,
    ),
    3: Book(
        id=3,
        title="The Return of the King",
        author="J.R.R. Tolkien",
        publication_year=1955,
        genre=Genre.FANTASY,
    ),
}

@router.get("")
async def get_books():
    """Retrieve all books."""
    return list(db.books.values())

@router.get("/{book_id}")
async def get_book(book_id: int):
    """Retrieve a specific book by ID."""
    book = db.books.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    """Create a new book."""
    if book.id in db.books:
        raise HTTPException(status_code=400, detail="Book with this ID already exists")
    db.books[book.id] = book
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=book.model_dump())

@router.put("/{book_id}")
async def update_book(book_id: int, book: Book):
    """Update an existing book by ID."""
    if book_id not in db.books:
        raise HTTPException(status_code=404, detail="Book not found")
    db.books[book_id] = book
    return book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    """Delete a book by ID."""
    if book_id not in db.books:
        raise HTTPException(status_code=404, detail="Book not found")
    del db.books[book_id]
