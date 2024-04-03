from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from sockets import router as socket_router

app = FastAPI()
app.include_router(socket_router)
# 경로, HTML response가 필요


@app.get("/")
def index():
    index_html = Path("index.html").read_text()
    return HTMLResponse(index_html)


# 실행 명령어: uvicorn main:app --reload
