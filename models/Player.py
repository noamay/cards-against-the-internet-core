import datetime

from pydantic import BaseModel


class Player(BaseModel):
    name: str
    id: str
    hand: list = []
    ap: int = 0
    last_poop: datetime.datetime
    admin: bool = False

    def draw_card_to_hand(self, card):  # should be implemented in game logic instead imo --> THATS EXACTLY WHY THE LOGIC WAS JUST TO RECEIVE A CARD.
        self.hand.append(card)
