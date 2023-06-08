from typing import Dict
from fastapi import WebSocket, WebSocketDisconnect


class WebSocketManager:
    def __init__(self):
        self.connections: Dict[str, WebSocket] = {}

    def add_connection(self, game_session_id: str, websocket: WebSocket):
        self.connections[game_session_id] = websocket

    def remove_connection(self, game_session_id: str):
        del self.connections[game_session_id]

    async def send_notification(self, game_session_id: str, message: str):
        websocket = self.connections.get(game_session_id)
        if websocket:
            await websocket.send_text(message)


async def on_connect(websocket: WebSocket):
    await websocket.accept()
    # Perform any necessary operations upon WebSocket connection


async def on_disconnect(websocket: WebSocket, game_session_id: str):
    pass
    # Perform any necessary cleanup or actions upon WebSocket disconnection
    # Remove the WebSocket connection from the WebSocket manager


async def on_receive(websocket: WebSocket, game_session_id: str, message: str):
    pass
    # Handle the received message from the WebSocket connection
    # Perform any necessary operations based on the received message
    # Send notifications or update the game state, etc.


async def on_receive_json(websocket: WebSocket, game_session_id: str, data: dict):
    pass
    # Handle the received JSON message from the WebSocket connection
    # Perform any necessary operations based on the received data
    # Send notifications or update the game state, etc.
