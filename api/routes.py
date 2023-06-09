from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from api.schemas import StartGameRequest, JoinGameRequest
from services.Game import create_game, join_game

router = APIRouter()


@router.post("/create-game")
async def create_game_route(game_request: StartGameRequest):
    return create_game(game_request)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Hello WebSocket!")
    await websocket.close()
