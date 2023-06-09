from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from api.web_socket import WebSocketManager, on_connect, on_disconnect, on_receive, on_receive_json
from api.schemas import StartGameRequest, JoinGameRequest
from services.Game import create_game, join_game

router = APIRouter()
websocket_manager = WebSocketManager()


@router.post("/create-game")
async def create_game_route(game_request: StartGameRequest):
    print(game_request)
    session = create_game(game_request)
    return session


@router.get("/join-game")
async def join_game_route(game_request: JoinGameRequest):
    return join_game(game_request)

@router.get("/test")
async def test(session_id: str):
    await websocket_manager.send_notification(session_id, "Hello World")
    return {"Status": "OK"}


@router.websocket("/ws/{game_session_id}")
async def websocket_endpoint(websocket: WebSocket, game_session_id: str):
    await on_connect(websocket)
    try:
        websocket_manager.add_connection(game_session_id, websocket)
        while True:
            data = await websocket.receive_text()
            await on_receive(websocket, game_session_id, data)
    except WebSocketDisconnect:
        await on_disconnect(websocket, game_session_id)
