from fastapi import FastAPI
from items import router as items_router
from users import router as users_router
import uvicorn

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):  # q: query
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="debug", reload=True)
