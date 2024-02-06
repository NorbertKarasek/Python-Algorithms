# Implementacja grafu za pomocą tablicy skrótów

class MangoSeller:
    def __init__(self, name, is_seller = False):
        self.name = name
        self.is_seller = is_seller

    def person_is_seller(self):
        if self.is_seller:
            return True

    def __repr__(self):
        return self.name


ja = MangoSeller('norbert')
alicja = MangoSeller('alicja')
bartek = MangoSeller('bartek')
cecylia = MangoSeller('cecylia')
janusz = MangoSeller('janusz')
patrycja = MangoSeller('patrycja')
tamara = MangoSeller('tamara')
jarek = MangoSeller('jarek', is_seller=True)
# Klasa i pare obiektów na potrzeby przeszukiwania wszerz

graph = {}
graph[ja] = [alicja, bartek, cecylia]
graph[bartek] = [janusz, patrycja]
graph[alicja] = [patrycja]
graph[cecylia] = [tamara, jarek]
graph[janusz] = []
graph[patrycja] = []
graph[tamara] = []
graph[jarek] = []

# wyszukiwanie wszerz z pomocą kolejki
from collections import deque

search_queue = deque()
search_queue += graph[ja]
print(search_queue)

def search_for_seller(search_queue): # Tu podajemy kolejkę w której jest tylko osoba która poszukuje sprzedawcy
    while search_queue:  # dopóki kolejka nie jest pusta
        person = search_queue.popleft()  # pobiera pierwszy element z kolejki
        if MangoSeller.person_is_seller(person):
            print(person.name.capitalize() + ' sprzedaje mango !')
            return True
        else:
            search_queue += graph[person]
    return False
# pamietajmy że ten graf jest skierowany, więc tutaj najlepiej będzie szukać od norberta, wtedy przeszuka całego grafa,
# w przypadku nieskierowanego nie miało by to różnicy, itak szukałby wszędzie

search_for_seller(search_queue) # dajemy mu naszą kolejkę w której jestem ja

name = "witek"