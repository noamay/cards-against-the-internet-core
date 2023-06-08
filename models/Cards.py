import json
import random
from abc import ABC

from pydantic import BaseModel

from utils.constants import CARDS_JSON_LOCATION, DEFAULT_PACK


class Card(ABC, BaseModel):
    text: str

    def __repr__(self):
        return self.text


class WhiteCard(Card):
    pass


class BlackCard(Card):
    pick: int

    def get_combination(self, white_card: WhiteCard) -> str:
        return self.text.replace("_", white_card.text)


class Deck(BaseModel):
    white_cards: list[WhiteCard] = []
    black_cards: list[BlackCard] = []

    def __init__(self, pack_ids: list[int] = DEFAULT_PACK, **data):
        super().__init__(**data)
        with open(CARDS_JSON_LOCATION, "r") as f:
            stock = json.load(f)
        stock_white_cards = stock.get("white")
        stock_black_cards = stock.get("black")
        white_cards_ids = [card_id for pack_id in pack_ids for card_id in
                           stock.get("packs", {})[pack_id].get("white", [])]
        black_cards_ids = [card_id for pack_id in pack_ids for card_id in
                           stock.get("packs", {})[pack_id].get("black", [])]
        self.white_cards = [WhiteCard(text=stock_white_cards[i]) for i in white_cards_ids]
        self.black_cards = [BlackCard(**stock_black_cards[i]) for i in black_cards_ids]

    def draw_black_card(self) -> BlackCard:
        if len(self.black_cards) == 0:
            raise NotEnoughCardsException(1, BlackCard)
        return self.black_cards.pop(random.randint(0, len(self.black_cards) - 1))

    def draw_white_cards(self, amount: int = 1) -> list[WhiteCard]:
        if amount > len(self.white_cards):
            raise NotEnoughCardsException(amount, WhiteCard)
        return [self.white_cards.pop(random.randint(0, len(self.white_cards) - 1)) for _ in
                range(amount)]


class NotEnoughCardsException(Exception):
    def __init__(self, amount: int, card_type: type):
        self.amount = amount
        self.card_type = card_type

    def __str__(self):
        return f"Not enough {self.card_type} cards in deck. Requested {self.amount} cards"

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    my_deck = Deck(DEFAULT_PACK)
    print(my_deck.black_cards)
    print(my_deck.draw_black_card())
