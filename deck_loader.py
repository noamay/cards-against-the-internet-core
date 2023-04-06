import json

# This is a script file for loading the cards JSON file into a dict of two lists - white and black cards.
DEFAULT_DECKS = [1, 2]


def load_deck(pack_ids: list[int]):
    """Load the deck from the JSON file."""
    with open("cah-all-compact.json", "r") as f:
        stock = json.load(f)
    stock_white_cards = stock.get("white")
    stock_black_cards = stock.get("black")
    white_cards_ids = [card_id for pack_id in pack_ids for card_id in
                       stock.get("packs", {})[pack_id].get("white", [])]
    black_cards_ids = [card_id for pack_id in pack_ids for card_id in
                       stock.get("packs", {})[pack_id].get("black", [])]
    deck = {"white": [stock_white_cards[i] for i in white_cards_ids],
            "black": [stock_black_cards[i] for i in black_cards_ids]}
    return deck


if __name__ == '__main__':
    my_deck = load_deck(DEFAULT_DECKS)
    print(my_deck)
