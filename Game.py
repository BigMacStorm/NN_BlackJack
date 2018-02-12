from Dealer import Dealer
from Deck import Deck
from player import Player


class Game:
    def __init__(self, nn, player_count = 3):
        self.deck = Deck()
        self.NN = nn
        self.Dealer = Dealer()
        self.Players = []
        for x in range(0, player_count):
            self.Players.append(Player(self, self.NN, 1000))
        self.done = False

    def play_hand(self):
        pass
