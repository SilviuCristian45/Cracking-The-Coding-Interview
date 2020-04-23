from enum import Enum

class Suit(Enum):
    DIAMOND = 0
    HEARTS = 1
    SPADES = 2
    CLUBS = 3
    
class Card():
    def __init__(self,number,s):
        self.suit = s
        self.number = number
    def Print(self):
        print("The card you drew")
        card_number = str(self.number)
        print(str(card_number) + " of " + str(self.suit.name))
        