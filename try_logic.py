import random
white_deck = [] #load deck json
black_deck = [] #load black deck
player_hand = []

class game:
    def deal_cards(self,turn):
        card = random.choice(white_deck)
        turn.append(card)
        white_deck.remove(card)
    
    def play_card(self,player_hand,card):
        player_hand.remove(card)
    

#maybe use gTTs to read out cards?