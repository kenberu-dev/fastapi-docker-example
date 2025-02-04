from fastapi import FastAPI, HTTPException
from book_schemas import BookSchema

app = FastAPI()

@app.post("/books/", response_model=BookResponseSchema)
def create_book(book: BookSchema):
    new_book_id = max([book.id for book in books], default=0) + 1
    new_book = BookResponseSchema(id=new_book_id, **book.model_dump())
    books.append(new_book)
    
    return new_book

@app.get("/books/", response_model=list[BookResponseSchema])
def read_books():
    return books

@app.get("/books/{book_id}", response_model=BookResponseSchema)
def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}", response_model=BookResponseSchema)
def update_book(book_id: int, book: BookSchema):
    for index, existing_book in enumerate(books):
        if existing_book.id == book_id:
            updated_book = BookResponseSchema(id=book_id, **book.model_dump())
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", response_model=BookResponseSchema)
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            book.pop(index)
            return book
    raise HTTPException(status_code=404, detail="Book not found")