from fastapi import FastAPI
from models.GameSession import GameSession
from api.schemas import StartGameRequest, JoinGameRequest
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix="/apiv2")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/api/new-game/")
async def start_new_session(data: StartGameRequest):
    session = GameSession(pack_ids=data.pack_ids, admin_name=data.admin_name,
                          admin_time_of_poop=data.admin_time_of_poop, max_rounds=data.max_rounds, max_ap=data.max_ap)
    # TODO - Start Session
    return {"message": f"Hello {data.admin_name}"}


@app.post("/api/join-game/")
async def join_session(data: JoinGameRequest):
    # TODO - Needs to be able to join a session and get a websocket connection
    print(data)
    # session = GameSession.get_game_session_by_id(data.session_id)
    # player = session.add_player(data.name, data.last_poop)
    return {"message": f"Hello {data.name}"}


@app.websocket("/ws")
async def websocket_endpoint(websocket):
    # TODO - WebSocket Interface for Screen & Players
    await websocket.accept()
    await websocket.send_text("Hello WebSocket!")
    await websocket.close()
