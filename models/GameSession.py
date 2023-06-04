import datetime

from pydantic import BaseModel

from utils.constants import SessionStatus
from models.Cards import Deck
from models.Player import Player
from models.Round import Round

from utils.utils import generate_random_id


class GameSession(BaseModel):
    deck: Deck
    admin: Player = None
    players: dict[str, Player] = {}
    max_rounds: int = 0  # Session Rounds Limit - 0 means no limit
    max_ap: int = 10  # Session AP Limit - 0 means no limit
    round_count: int = 0
    past_rounds: list[Round] = []
    current_round: Round = None
    status: SessionStatus = SessionStatus.WAITING
    turn_list: list[str] = []
    current_tzar_index: int = 0
    session_id: str

    def _get_next_tzar(self):
        self.current_tzar_index += 1
        if self.current_tzar_index >= len(self.players):
            self.current_tzar_index = 0
        return self.players[self.turn_list[self.current_tzar_index]]

    def add_player(self, player_name: str, time_of_poop: datetime.datetime, admin=False) -> Player:
        new_player = Player(name=player_name, last_poop=time_of_poop,
                            id=generate_random_id(6, [p.id for p in self.players]))
        new_player.admin = admin
        self.players[new_player.id] = new_player
        return new_player

    def start_session(self):
        self.turn_list = sorted([p for p in self.players.keys()], key=lambda p: self.players[p].last_poop, reverse=True)
        for player in self.players.values():
            player.hand = self.deck.draw_white_cards(amount=10)
        self.status = SessionStatus.STARTED
        self.start_round()

    def start_round(self, tzar: Player = None):
        black_card = self.deck.draw_black_card()
        # current_round = Round(black_card, self.players, tzar or self._get_next_tzar())
        # TODO - start round

    @staticmethod
    def get_game_session_by_id(session_id: str) -> "GameSession":
        # TODO - Get session by ID
        pass
