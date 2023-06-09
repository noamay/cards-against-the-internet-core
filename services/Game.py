import asyncio

from models.Cards import Deck
from models.GameSession import GameSession
from api.schemas import StartGameRequest, JoinGameRequest
from utils.utils import generate_random_id

game_sessions = {}


def create_game(data: StartGameRequest):
    game_deck = Deck(pack_ids=data.pack_ids)
    session = GameSession(deck=game_deck, max_rounds=data.max_rounds, max_ap=data.max_ap,
                          session_id=generate_random_id(6, list(game_sessions.keys())))
    session.add_player(player_name=data.admin_name, time_of_poop=data.admin_time_of_poop, admin=True)
    game_sessions[session.session_id] = session
    return session


async def join_game(data: JoinGameRequest):
    session = game_sessions.get(data.session_id, None)
    if not session:
        raise SessionNotFoundException
    # TODO - add logic for joining a game in progress
    session.add_player(player_name=data.name, time_of_poop=data.last_poop)
    return session


class SessionNotFoundException(Exception):
    # No session found with the given ID
    pass

