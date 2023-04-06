import json
import random

from constants import CARDS_JSON_LOCATION

DEFAULT_PACK = [1, 2]


class Card:
    def __init__(self, color):
        self.color = color
        # not sure what else for now

    @staticmethod
    def get_random_card(deck):
        return random.choice(deck)


class Deck:
    def __init__(self, pack_ids: list[int]):
        self.pack_ids = pack_ids
        self.deck = {}
        self.load_deck()

    def load_deck(self):
        with open(CARDS_JSON_LOCATION, "r") as f:
            stock = json.load(f)
        stock_white_cards = stock.get("white")
        stock_black_cards = stock.get("black")
        white_cards_ids = [card_id for pack_id in self.pack_ids for card_id in
                           stock.get("packs", {})[pack_id].get("white", [])]
        black_cards_ids = [card_id for pack_id in self.pack_ids for card_id in
                           stock.get("packs", {})[pack_id].get("black", [])]
        self.deck = {"white": [stock_white_cards[i] for i in white_cards_ids],
                     "black": [stock_black_cards[i] for i in black_cards_ids]}
        return self.deck

    def get_random_card(self, black_card=False):
        return random.choice(self.deck.get('white') if not black_card else self.deck.get('black'))


if __name__ == '__main__':
    my_deck = Deck(DEFAULT_PACK)
    print(my_deck.get_random_card(black_card=True))
