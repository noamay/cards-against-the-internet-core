import datetime
import random
from models.Cards import Deck


class Player:
    def __init__(self, name: str, last_poop: datetime.datetime, player_id: int):
        self.name = name
        self.id = player_id
        self.hand = []
        self.ap = 0
        self.last_poop = last_poop

    def draw_card_to_hand(self, card):  # should be implemented in game logic instead imo --> THATS EXACTLY WHY THE LOGIC WAS JUST TO RECEIVE A CARD.
        self.hand.append(card)

    def calc_AP(self, name):
        a = 0  # not sure what to do here yet

    def reset_hand(self):
        self.hand = []
