import json
import random
from abc import ABC

from utils.constants import CARDS_JSON_LOCATION, CardType, DEFAULT_PACK


class Card(ABC):
    def __init__(self, text: str):
        self.text = text

    def __repr__(self):
        return self.text


class WhiteCard(Card):
    def __init__(self, card: str):
        super().__init__(card)
        self.type = CardType.WHITE


class BlackCard(Card):
    def __init__(self, card: dict):
        super().__init__(card.get('text'))
        self.pick = card.get('pick')
        self.type = CardType.BLACK

    def get_combination(self, white_card: WhiteCard) -> str:
        return self.text.replace("_", white_card.text)


class Deck:
    def __init__(self, pack_ids: list[int]):
        self.pack_ids = pack_ids
        self.white_cards = []
        self.black_cards = []
        self._load_deck()

    def _load_deck(self):
        with open(CARDS_JSON_LOCATION, "r") as f:
            stock = json.load(f)
        stock_white_cards = stock.get("white")
        stock_black_cards = stock.get("black")
        white_cards_ids = [card_id for pack_id in self.pack_ids for card_id in
                           stock.get("packs", {})[pack_id].get("white", [])]
        black_cards_ids = [card_id for pack_id in self.pack_ids for card_id in
                           stock.get("packs", {})[pack_id].get("black", [])]
        self.white_cards = [WhiteCard(stock_white_cards[i]) for i in white_cards_ids]
        self.black_cards = [BlackCard(stock_black_cards[i]) for i in black_cards_ids]

    def draw_random_cards(self, card_type: CardType = CardType.WHITE, amount: int = 1) -> list[Card] or Card:
        if card_type == CardType.WHITE:
            return [self.white_cards.pop(random.randint(0, len(self.white_cards) - 1)) for _ in
                    range(amount)]
        return self.black_cards.pop(random.randint(0, len(self.black_cards) - 1))


if __name__ == '__main__':
    my_deck = Deck(DEFAULT_PACK)
    print(my_deck.black_cards)
    print(my_deck.draw_random_cards(CardType.WHITE))
