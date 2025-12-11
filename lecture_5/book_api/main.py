from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from connect import SessionLocal, engine
import models
import operations

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books/", response_model=list[operations.Book])
def read_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()


@app.post("/books/", response_model=operations.Book)
def create_book(book: operations.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/{book_id}", response_model=operations.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).get(book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.put("/books/{book_id}", response_model=operations.Book)
def update_book(book_id: int, book: operations.BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).get(book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    for key, value in book.dict().items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).get(book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted"}

@app.get("/books/search", response_model=list[operations.Book])
def search_books(
    title: str | None = Query(None),
    author: str | None = Query(None),
    year: int | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.Book)

    if title:
        query = query.filter(models.Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(models.Book.year == year)

    return query.all()
