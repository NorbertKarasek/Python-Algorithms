import random

#   Listy - Listy.py

# Tak tworzymy listę
fruit = list()
fruit1 = []
fruit2 = ['apple', 'banana', 'cherry', 'pomelo', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'watermelon']
different_types = [1, True, 'apple', 3.14]  # Lista może zawierać różne typy danych

# Tak dodajemy element do listy
fruit.append('apple')
fruit.append('orange')
fruit.append('pear')

print(fruit)
print(fruit1)
print(fruit2)
print(different_types)

# Dodawanie list
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