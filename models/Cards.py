import random

DEFAULT_PACK = ['something', 'something else']


class Card:
    def __init__(self, color):
        self.color = color
        # not sure what else for now

    @staticmethod
    def get_random_card(deck):
        return random.choice(deck)


class Deck:
    def __init__(self, packs: list = DEFAULT_PACK, black_deck=False):
        self.packs = packs
        self.black_deck = black_deck
        self.deck = []
        self.load_deck()

    def load_deck(self):
        # TODO - load deck from json
        pass

    def get_random_card(self):
        return random.choice(self.deck)
