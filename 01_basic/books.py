from fastapi import FastAPI, APIRouter

# 로컬메모리 DB - 서버 종료시 데이터 사라짐
BOOKS = [
    {
        "id": 1,
        "title": "Sapiens",
        "author": "유발하라리",
        "url": "https://www.yes24.com/sapiens",
    }
]

app = FastAPI()
router = APIRouter()


@router.get("/", status_code=200)
def main():
    return {"msg": "welocome to the book world!"}


# 전체 책 데이터 조회
@router.get("/api/v1/books", status_code=200)
def get_all_books() -> list:
    return BOOKS  # [{book1}, {book2}]


# 특정 책 데이터 조회
@router.get("/api/v1/books/{book_id}", status_code=200)
def get_book(book_id: int):
    book = next((book for book in BOOKS if book["id"] == book_id), None)

    if book:
        return book
    return {"error": f"book not found, ID: {book_id}"}


@router.post("/api/v1/books/")
def create_book(book: dict):
    BOOKS.append(book)
    return book


@router.put("/api/v1/books/{book_id}")
def update_book(book_id: int, book_update: dict):
    book = next((book for book in BOOKS if book["id"] == book_id), None)
    for key, val in book_update.items():
        if key in book:
            book[key] = val
    return book


@router.delete("/api/v1/books/{book_id}")
def delete_book(book_id: int):
    global BOOKS

    BOOKS = [item for item in BOOKS if item["id"] != book_id]
    return {"msg": f"successfully delete book, ID: {book_id}"}


app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("books:app", port=8000, log_level="debug", reload=True)
