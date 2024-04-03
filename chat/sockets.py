# websocket 연결 -> ws://127.0.0.1/ws
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from connection import manager
from models import Message
from dependencies import get_username


router = APIRouter()


@router.websocket("/ws/{token}")  # 웹소켓에 연결하겠다
async def websocket_endpoint(websocket: WebSocket, token: str):
    username = get_username(token)
    await manager.connect(websocket)

    try:
        while True:  # 소켓이 연결되어 있으면
            data = await websocket.receive_text()  #  유저에게 받은 텍스트
            message = Message(username=username, text=data)  #
            await manager.broadcast(
                message.model_dump_json()
            )  # 받은 텍스트 다른 사람들에게 보내주기
    except WebSocketDisconnect:
        manager.disconnect(websocket)
