class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.awesome_points = 0
    

    def draw_card_to_hand(self,card):
        self.hand.append(card)

    
    def calc_AP(self,name):
        a = 0 #not sure what to do here yet
    
    def reset_hand(self):
        self.hand = []