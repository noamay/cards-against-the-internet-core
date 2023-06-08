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
    # TODO - Doesn't work yet
    session_id: str
    admin_name: str
    max_rounds: int
    max_ap: int
    status: str
    players: list[dict]
    current_round: dict
    past_rounds: list[dict]

    @staticmethod
    def from_game_session(game_session: GameSession):
        pass
        return GameSessionResponse(
            session_id=game_session.session_id,
            admin_name=game_session.admin.name,
            max_rounds=game_session.max_rounds,
            max_ap=game_session.max_ap,
            status=game_session.status.value,
            players=[p.to_dict() for p in game_session.players],
            current_round=game_session.current_round.to_dict(),
            past_rounds=[r.to_dict() for r in game_session.past_rounds]
        )