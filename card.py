from enum import Enum


class Suit(Enum):
    Spade = 0
    Club = 1
    Heart = 2
    Diamond = 3


class Card:

    def __init__(self, suit, value):
        self.suit = Suit(suit)
        self.color = 'b' if self.suit.__value__ < 2 else 'r'
        self.value = value


