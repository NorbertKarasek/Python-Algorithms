# Karty do gry

class Card:
    suits = ['pik', 'trefl', 'karo', 'kier']  # lista kolorów
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'walet', 'dama', 'król', 'as']  # lista wartości

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        show = str(self.values[self.value] + ' ' + self.suits[self.suit])
        return show