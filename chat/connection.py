# websocker 연결관리
from fastapi import WebSocket
from typing import List


class ConnectionManager:
    # 연결, 끊기, 전달하기 세가지 함수 필요
    def __init__(self):
        self.active_connections: List(WebSocket) = []  # [websocker, websocket, ..]

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    # 소켓을 통해 들어온 데이터를 각 소켓으로 전송하는 역할
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()
