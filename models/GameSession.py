from models.Cards import Deck
from models.Player import Player


class GameSession:
    def __init__(self, pack_ids: list[int], players: list[Player], admin: Player, max_rounds: int = 0,
                 max_ap: int = 15):
        self.deck = Deck(pack_ids)
        self.players = sorted(players, key= lambda p: p.last_poop, reverse=True)
        self.admin = admin
        self.max_rounds = max_rounds
        self.max_ap = max_ap
        self.round = 0
        self.current_tzar = 0
        self.black_card = None
        self.white_cards = []
        self.winner = None

    def _get_current_tzar(self):
        return self.players[self.current_tzar]
