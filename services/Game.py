from models.GameSession import GameSession
from api.schemas import StartGameRequest, JoinGameRequest
from fastapi.middleware.cors import CORSMiddleware
from fastapi import WebSocket, WebSocketDisconnect
from main import app

game_sessions = {}


def create_game(data: StartGameRequest):
    session = GameSession(pack_ids=data.pack_ids, admin_name=data.admin_name,
                          admin_time_of_poop=data.admin_time_of_poop, max_rounds=data.max_rounds, max_ap=data.max_ap)
    # TODO - Start Session
    game_sessions[session.session_id] = session
    return {"message": f"Hello {data.admin_name}"}
