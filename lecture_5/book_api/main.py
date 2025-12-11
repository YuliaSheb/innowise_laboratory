from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from connect import SessionLocal, engine
from models import Book

Book.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/")
def add_book(title: str, author: str, year: int | None = None, db: Session = Depends(get_db)):
    book = Book(title=title, author=author, year=year)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@app.get("/books/")
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}

@app.put("/books/{book_id}")
def update_book(
    book_id: int,
    title: str | None = None,
    author: str | None = None,
    year: int | None = None,
    db: Session = Depends(get_db)
):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if title is not None:
        book.title = title
    if author is not None:
        book.author = author
    if year is not None:
        book.year = year

    db.commit()
    db.refresh(book)
    return book

@app.get("/books/search/")
def search_books(
    title: str | None = None,
    author: str | None = None,
    year: int | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Book)

    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(Book.year == year)

    return query.all()
