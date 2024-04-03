from fastapi import APIRouter
from typing import List, Optional
from models import Book, CreateBook, SearchBooks

route = APIRouter()
books: List[Book] = []  # books: 리스트안에 Book 객체가 담기게 된다.


@route.post("/")
def create_book(
    book: CreateBook,
) -> (
    Book
):  # CreateBook객체(id불포함)를 book에 입력받아서 Book객체(자동생성 ID포함)로 return
    book = Book(id=len(books) + 1, **book.model_dump())
    books.append(book)
    return book


@route.get("/search/")
def search_books(
    keyword: Optional[str] = None, max_results: int = 10
) -> SearchBooks:  # [Book, Book, ...]
    # max_results: int =10 -> 페이지네이션 최대 10개 보여줘
    # keyword있으면 [book for book in books if keyword in book.title] 수행, keyword 없으면 books 그대로 내려줘
    search_result = (
        [book for book in books if keyword in book.title] if keyword else books
    )

    return SearchBooks(results=search_result[:max_results])  # [Book, Book, ...]
