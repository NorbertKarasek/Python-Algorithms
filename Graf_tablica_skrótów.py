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


norbert = MangoSeller('norbert')
alicja = MangoSeller('alicja')
bartek = MangoSeller('bartek')
cecylia = MangoSeller('cecylia')
janusz = MangoSeller('janusz')
patrycja = MangoSeller('patrycja')
tamara = MangoSeller('tamara')
jarek = MangoSeller('jarek', is_seller=True)
# Klasa i pare obiektów na potrzeby przeszukiwania wszerz

graph = {}
graph[norbert] = [alicja, bartek, cecylia]
graph[bartek] = [janusz, patrycja]
graph[alicja] = [patrycja]
graph[cecylia] = [tamara, jarek]
graph[janusz] = []
graph[patrycja] = []
graph[tamara] = []
graph[jarek] = []

# wyszukiwanie wszerz z pomocą kolejki
from collections import deque

def search_for_seller(name): # Tu podajemy osobę która szuka sprzedawcy, i od niej zaczniemy szukać po znajomych
    search_queue = deque() # tworzymy kolejkę
    search_queue += graph[name] # dodajemy do niej naszą osobę (obiekt)
    searched = [] # tworzymy pustą listę na sprawdzone osoby

    while search_queue:  # dopóki kolejka nie jest pusta
        person = search_queue.popleft() # pobiera pierwszy element z kolejki
        if person not in searched: # jeżeli osoba nie była już przeszukana
            if MangoSeller.person_is_seller(person):
                print(person.name.capitalize() + ' sprzedaje mango !')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print(f'{name} nikt z twoich znajomych nie sprzedaje mango')
    return False

# pamietajmy że ten graf jest skierowany, więc tutaj najlepiej będzie szukać od norberta, wtedy przeszuka całego grafa,
# w przypadku nieskierowanego nie miało by to różnicy, itak szukałby wszędzie


search_for_seller(norbert) # dajemy mu naszą osobę która szuka sprzedawcy