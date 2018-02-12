from random import random


class Player:
    def __init__(self, game, nn, chest = 1000):
        self.game = game
        self.chest = chest
        self.NN = nn

    @staticmethod
    def decide():
        return random % 2, random % 100/100.0
