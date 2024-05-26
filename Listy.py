import random
import datetime


#   Listy - Listy.py

# Tworzenie listy
fruit = list()
fruit1 = []
fruit2 = ['apple', 'banana', 'cherry', 'pomelo', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'watermelon']
different_types = [1, True, 'apple', 3.14]  # Lista może zawierać różne typy danych

# Doodanie elementu do listy
fruit.append('apple')
fruit.append('orange')
fruit.append('pear')

print(fruit)
print(fruit1)
print(fruit2)
print(different_types)

# Dodawanie list do siebie
fruit3 = fruit + fruit1 + fruit2
print(fruit3)

# Tworzenie listy z zakresu
numbers = list(range(10)) # Tworzy listę od 0 do 9
print(numbers)
# Twożenie listy z zakresu z krokiem
numbers = list(range(0, 100, 10)) # Tworzy listę od 0 do 100 z krokiem 10

# Tak usuwamy element z listy
fruit2.remove('orange') # Usuwanie elementu po wartości
del fruit2[0] # Usuwanie elementu po indeksie
print(fruit2)
fruit2.pop() # Usuwanie ostatniego elementu
fruit2.pop(3) # Usuwanie elementu po indeksie
print(fruit2.pop(4)) # Usuwanie elementu po indeksie i wyświetlenie/użycie go np:
fruit.append(fruit2.pop(4)) # Usuwanie elementu po indeksie i dodanie go do innej listy
print(fruit)

# Wyświetlanie elementów listy
print('element o indeksie 2: '+ fruit2[2])
print(f'elementy z zakresu indeksów 2:5: {fruit2[2:5]}')

# Iterowanie po liście
for i in fruit2:
    print(i) # Wyświetli wszystkie elementy listy

# Sprawdzanie czy element znajduje się w liście
if 'apple' in fruit2:
    print('apple znajduje się na liście')

print('cherry' in fruit2)  # True
print('samochód' in fruit2)  # False
print('samochód' not in fruit2)  # True


#Znajdywanie indeksu elementu
print(fruit2.index('cherry')) #Zwróci 2


#Zmiana elementu w liście
print('przed podmianą: '+ fruit2[2])
fruit2[2] = 'cherry'
print('po podmianie: '+ fruit2[2])

#Długość listy
print('długość listy: '+ str(len(fruit2)))
print(f'długość listy: {len(fruit2)}')

try:
    print(fruit2[17]) #Wyświetli błąd, bo lista ma tylko 14 elementów
except IndexError:
    print('Nie ma takiego indeksu')

#Operacje na każdym elemencie listy
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)

for num in numbers:
    i=0
    numbers[i] = numbers[i] * 2
    i+=1
print(numbers)


#Operacje na co drugim elemencie listy
for i in range(0,len(numbers),2):
    numbers[i] //= 2
print(numbers)

#Czyszczenie listy
fruit2.clear()

#Sprawdzanie czy lista jest pusta
print('lista jest pusta: '+ str(len(fruit2) == 0))

# Zgadywanka

'''
while True:
    print('Zgadnij owoc')
    guess = input()
    if guess in fruit3:
        print('Zgadłeś!')
        break
    else:
        print('Spróbuj jeszcze raz')
'''

# Operacje na listach
numbers.reverse() # Odwraca listę
print(numbers)
random.shuffle(numbers) # Tasuje listę
print(numbers)
numbers.sort() # Sortuje listę
print(numbers)
numbers.sort(reverse=True) # Sortuje listę malejąco
print(numbers)

# Kopiowanie listy
numbers2 = numbers.copy()
numbers3 = numbers[:]
numbers4 = list(numbers)
numbers.append(200)
numbers.append(300)
print(numbers) # tą listę zmieniliśmy
print(numbers2) # ta lista nie zmieniła się

# Listy wielowymiarowe
multi = [[1,2,3],[4,5,6],[7,8,9]]
print(multi[1][1]) # Wyświetli 5

# Listy składane
numbers = [x for x in range(10)] # Tworzy listę od 0 do 9
print(numbers)
numbers = [x*2 for x in range(10)] # Tworzy listę od 0 do 18 z krokiem 2
print(numbers)
numbers = [x for x in range(0,20,2)] # Ten sam efekt co powyżej
print(numbers)
numbers = [x for x in range(10) if x % 2 == 0] # Tworzy listę liczb parzystych od 0 do 9
print(numbers)
numbers = [x for x in range(10) if x % 2 != 0] # Tworzy listę liczb nieparzystych od 0 do 9
print(numbers)
numbers = [x for x in range(100) if x % 2 == 0 if x % 3 == 0] # Tworzy listę liczb podzielnych przez 2 i 3 od 0 do 99
print(numbers)
numbers = [x*10 if x % 2 == 0 else 'nieparzysta' for x in range(10)] # Tworzy listę liczb parzystych od 0 do 9*10, a nieparzyste zamienia na napis
print(numbers)

# Listy składane wielowymiarowe
multi = [[x*y for x in range(10)] for y in range(10)]
print(multi)

''' KROTKI (TUPLE) - niezmienne listy - nie można dodawać, usuwać ani zmieniać elementów '''
print('\nKROTKI (TUPLE)\n')

# Tworzenie krotki
fruit = ('apple', 'orange', 'pear')
fruit1 = 'apple', 'orange', 'pear' # Można tworzyć bez nawiasów
fruit2 = 'apple', # Krotka z jednym elementem
fruit3 = () # Pusta krotka
fruit4 = tuple() # Pusta krotka
player1 = ('Michael', 'Jordan', 23, 1963, False) # Krotka z różnymi typami danych

print(fruit)
print(fruit1)
print(fruit2)
print(fruit3)
print(fruit4)
print(f'Player: {player1[0]} {player1[1]} \nNumber: {player1[2]} \nAge: {datetime.datetime.now().year - player1[3]} \nActive: {player1[4]}')

# Wyświetlanie elementów krotki
print(fruit[1]) # Wyświetli orange
print(fruit[1:3]) # Wyświetli zakres 1:3 ('orange', 'pear')

# Iterowanie po krotce
for i in range(len(fruit)):
    print(fruit[i].upper()) # Wyświetli elementy krotki z dużych liter

for i in fruit:
    print(i)

# Sprawdzanie czy element znajduje się w krotce
print('apple' in fruit) # True
print('apple' not in fruit) # False

# Znajdywanie indeksu elementu
print(fruit.index('orange')) # 1

# Długość krotki
print(len(fruit))

# Krotki składane
numbers = tuple(x for x in range(10)) # Tworzy krotkę od 0 do 9
print(numbers)
numbers = tuple(x*2 for x in range(10)) # Tworzy krotkę od 0 do 18 z krokiem 2
print(numbers)
numbers = tuple(x for x in range(0,20,2)) # Tworzy krotkę od 0 do 18 z krokiem 2
print(numbers)

