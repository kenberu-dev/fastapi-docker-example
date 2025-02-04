from fastapi import FastAPI, HTTPException
from book_schemas import BookSchema

app = FastAPI()

@app.post("/books/", response_model=BookSchema)
def create_book(book: BookSchema):
    return book