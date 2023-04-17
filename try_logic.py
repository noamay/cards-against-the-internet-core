import random
from models.Player import Player
from models.Cards import Deck
from models.GameSession import GameSession

gs = GameSession()

class Game_Logic:
    def deal_cards(self, turn):
        for player in gs.players:
            while len(player.hand) < 10:
                Player.draw_card_to_hand()


    def play_card(self, player_hand, card):
        player_hand.remove(card)

# maybe use gTTs to read out cards?
