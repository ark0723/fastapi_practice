from fastapi import FastAPI
from routes.users import router as user_router
from routes.items import router as item_router

app = FastAPI()
app.include_router(user_router)
app.include_router(item_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
