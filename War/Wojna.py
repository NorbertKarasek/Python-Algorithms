# Game of War

from War.Gracz import Player
from War.Talia import Deck

class Game:
    def __init__(self):
        name1 = input('Imię gracza 1: ')
        name2 = input('Imię gracza 2: ')
        self.deck = Deck()
        self.deck.shuffle()
        self.p1 = Player(name1.title())
        self.p2 = Player(name2.title())
        print('Grać będą ' + name1 + ' i ' + name2)
        print('Karty rozdane')

    def wins(self,winner):
        w = '{} wygrywa tę rundę'
        w = w.format(winner)
        print(w)

    def draw(self,p1n,p1c,p2n,p2c):
        d = '{} - {}  |  {} - {}'
        d = d.format(p1n, p1c, p2n, p2c) # player1name, player1card ...
        print(d)

    def winner(self,p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name

        return False

    def play_game(self):
        cards = self.deck.cards
        print('Zaczynamy!')
        while len(cards) >= 2:
            start = input('\nEnter by kontynuować, Q - koniec gry:')
            if start.lower() == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
            print(f'{self.p1.name}: {self.p1.wins} | {self.p2.name}: {self.p2.wins}')
        big_winner = self.winner(self.p1, self.p2)
        if big_winner:
            print('\n ***** Koniec gry. {} wygrał! *****'.format(big_winner))
            print(f'{big_winner} zdobył {abs(self.p1.wins - self.p2.wins)} punktów więcej niż przeciwnik.')
        else:
            print('\n***** Koniec gry. Remis! *****')
        print('Wynik: ' + self.p1.name + ': ' + str(self.p1.wins) + ' | ' + self.p2.name + ': ' + str(self.p2.wins))