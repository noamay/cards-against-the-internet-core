import datetime

from pydantic import BaseModel
from pydantic.class_validators import Optional


class StartGameRequest(BaseModel):
    pack_ids: list[int]
    admin_name: str
    admin_time_of_poop: datetime.datetime
    max_rounds: Optional[int] = 15  # 0 means no limit
    max_ap: Optional[int] = 10  # 0 means no limit


class PlayerRequest(BaseModel):
    name: str
    last_poop: datetime.datetime
    session_id: str
