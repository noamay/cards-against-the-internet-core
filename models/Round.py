from models.Cards import BlackCard, WhiteCard
from models.Player import Player


class Round:
    def __init__(self, black_card: BlackCard, players: list[Player], tzar: Player):
        self.players = players
        self.submissions = {}
        self.winner = None
        self.tzar = tzar
        self.black_card = black_card

    def add_submission(self, player: Player, submission: WhiteCard or [WhiteCard]):
        if player not in self.players:
            raise ValueError("Player not in round")
        if player in self.submissions:
            raise ValueError("Player already submitted")
        if isinstance(submission, WhiteCard):
            if submission not in player.hand:
                raise ValueError("Player does not have that card")
            if self.black_card.pick != 1:
                raise ValueError("Black card requires multiple cards")
            player.hand.remove(submission)
            submission = [submission]
        else:
            if len(submission) != self.black_card.pick:
                raise ValueError("Wrong number of cards submitted")
            for card in submission:
                if card not in player.hand:
                    raise ValueError("Player does not have that card")
                player.hand.remove(card)
        self.submissions[player] = submission
        if len(self.submissions) == len(self.players) - 1:
            self._choose_winner()

    def _choose_winner(self):
        # TODO - WebSocket broadcast to tzar & screen to choose winner
        pass

    def start(self):
        # TODO - WebSocket broadcast to players & screen to submit cards
        pass
