import datetime
from pydantic import BaseModel
from pydantic.class_validators import Optional

from models.GameSession import GameSession
from utils.constants import DEFAULT_PACK


class StartGameRequest(BaseModel):
    pack_ids: list[int] = DEFAULT_PACK
    admin_name: str
    admin_time_of_poop: datetime.datetime
    max_rounds: Optional[int] = 15  # 0 means no limit
    max_ap: Optional[int] = 10  # 0 means no limit


class JoinGameRequest(BaseModel):
    name: str
    last_poop: datetime.datetime
    session_id: str


class GameSessionResponse(BaseModel):
    session_id: str
    max_rounds: int
    max_ap: int
    status: str
    players: dict

    @staticmethod
    def from_game_session(game_session: GameSession):
        return GameSessionResponse(
            session_id=game_session.session_id,
            max_rounds=game_session.max_rounds,
            max_ap=game_session.max_ap,
            status=game_session.status.value,
            players={p.id: {'name': p.name, 'ap': p.ap, 'is_admin': p.admin} for p in game_session.players.values()},
        )
