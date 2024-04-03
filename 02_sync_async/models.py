from pydantic import BaseModel
from typing import Optional, List


class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None  # str로 받되, 없으면 None으로 한다


class CreateBook(BaseModel):
    title: str
    author: str
    description: Optional[str] = None  # str로 받되, 없으면 None으로 한다


class SearchBook(BaseModel):
    results: Optional[Book]


class SearchBooks(BaseModel):
    results: List[Book]  # [Book, Book, Book, ...]
