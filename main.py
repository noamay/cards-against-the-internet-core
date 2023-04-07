import datetime

from fastapi import FastAPI
from typing import List

from models.GameSession import GameSession
from models.Requests import StartGameRequest, PlayerRequest

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/api/new_game/")
async def start_new_session(data: StartGameRequest):
    session = GameSession(pack_ids=data.pack_ids, admin_name=data.admin_name,
                          admin_time_of_poop=data.admin_time_of_poop, max_rounds=data.max_rounds, max_ap=data.max_ap)
    # TODO - Start Session
    return {"message": f"Hello {data.admin_name}"}

@app.post("/api/join_game/")
async def join_session(data: PlayerRequest):
    # TODO - Needs to be able to join a session and get a websocket connection
    session = GameSession.get_game_session_by_id(data.session_id)
    player = session.add_player(data.name, data.last_poop)
    pass


@app.websocket("/ws")
async def websocket_endpoint(websocket):
    # TODO - WebSocket Interface for Screen & Players
    await websocket.accept()
    await websocket.send_text("Hello WebSocket!")
    await websocket.close()
