from card import Card
import random


class Deck:
    def add_standard(self):
        for x in range(0, 13):
            for y in range(0, 4):
                print("adding " + str(x+1) + " " + str(y))
                self.deck.append(Card(y, x+1))

    def __init__(self, count = 3):
        self.deck = []
        for x in range(0, count):
            self.add_standard()

    def shuffle(self):
        random.shuffle(self.deck)

