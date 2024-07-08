# Talia kart

from random import shuffle
from War.Karty import Card

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))

    def __repr__(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()