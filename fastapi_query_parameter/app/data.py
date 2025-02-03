from typing import Optional

class Book:
    def __init__(self, id: str, title: str, category: str):
        self.id = id
        self.title = title
        self.category = category

books = [
    Book("1", "Python入門", "technical"),
    Book("2", "はじめてのプログラミング", "technical"),
    Book("3", "すすむ巨人", "comic"),
    Book("4", "DBおやじ", "comic"),
    Book("5", "週刊ダイヤモンド", "magazine"),
    Book("6", "ザ・社長", "magazine"),
]

def get_books_by_category(
        category: Optional[str] = None
    ) -> list[Book]:
    if category is None:
        return books
    else:
        return [book for book in books if book.category == category]