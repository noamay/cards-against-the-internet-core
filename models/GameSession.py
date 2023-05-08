import datetime
import string
import secrets

from constants import CardType, SessionStatus
from models.Cards import Deck
from models.Player import Player
from models.Round import Round


class GameSession:
    def __init__(self,session_id, pack_ids: list[int], admin_name: str, admin_time_of_poop: datetime.datetime,
                 max_rounds: int = 0, max_ap: int = 10):
        self.deck = Deck(pack_ids)
        self.admin = Player(admin_name, admin_time_of_poop, 0)
        self.players = [self.admin]
        self.max_rounds = max_rounds  # Session Rounds Limit - 0 means no limit
        self.max_ap = max_ap  # Session AP Limit - 0 means no limit
        self.round_count = 0
        self.past_rounds = []
        self.current_round = None
        self.status = SessionStatus.WAITING
        self.current_tzar_index = 0
#        if session_id is None:
#            session_id = self.generate_random_session_id()
        self.session_id = self.generate_random_session_id()
        # TODO - Generate Session ID

    def _get_next_tzar(self):
        self.current_tzar_index += 1
        if self.current_tzar_index >= len(self.players):
            self.current_tzar_index = 0
        return self.players[self.current_tzar_index]

    def add_player(self, player_name: str, player_time_of_poop: datetime.datetime) -> Player:
        new_player = Player(player_name, player_time_of_poop, len(self.players) + 1)
        self.players.append(new_player)
        return new_player

    def start_session(self):
        self.players.sort(key=lambda p: p.last_poop, reverse=True)
        for player in self.players:
            player.hand = self.deck.draw_random_cards(amount=10)
        self.status = SessionStatus.STARTED
        self.start_round()

    def start_round(self, tzar: Player = None):
        black_card = self.deck.draw_random_cards(card_type=CardType.BLACK)
        current_round = Round(black_card, self.players, tzar or self._get_next_tzar())
        # TODO - start round

#    @staticmethod
#    def get_game_session_by_id(session_id: str) -> "GameSession":
        # TO#DO - Get session by ID
#
#        pass

    @staticmethod
    def get_game_session_by_id(session_id: str) -> "GameSession":
        game_session_id = GameSession.get(session_id) #Get session by ID
        if game_session_id is None:
            print(f"Game session with ID '{session_id}' not found.") #Do something
        else:
            return game_session_id

    @staticmethod
    def generate_random_session_id(length: int = 6) -> str:
        characters = string.ascii_letters + string.digits
        session_id = ''.join(secrets.choice(characters) for _ in range(length)) #Generate a secure random session ID
        return session_id