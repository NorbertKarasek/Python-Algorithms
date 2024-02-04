
# tablica skrótów z cenami  oraz nazwami owoców, owoc-klucz, cena-wartość
fruits = {'banana': 1.76,
          'apple': 4.23,
          'strawberry': 2.25,
          'pineapple': 7.70}

fruits2= {'coconut': 8.25,
          'banana': 3.40} # do późniejszego update()


print(fruits['banana'])#zwraca wartość klucza, 1.76
print(fruits['apple'])
print(fruits)
# zwraca słownik/tablice skrótów {'banana': 1.76, 'apple': 4.23, 'strawberry': 2.25, 'pineapple': 7.7}

fruits_keys = fruits.keys()
print(fruits_keys)
# keys() zwraca same klucze słownika, dict_keys(['banana', 'apple', 'strawberry', 'pineapple'])

fruit_values = fruits.values()
print(fruit_values)
# values() zwraca same wartości słwonika, dict_values([1.76, 4.23, 2.25, 7.7])

fruits_viev = fruits.items()
print(fruits_viev)
#zwraca listę tupli[(klucz, wartość)] które są zawartością słownika fruits []-lista ()-tuple

#tuple możemy przeiterować i stworzyć z nich osobne listy
fruits_list = []
fruits_prices = []
for fruit, price in fruits_viev:
    fruits_list.append(fruit)
    fruits_prices.append(price)

print('\n-osobne listy z kluczem i z wartośćią-')
print(fruits_list)
print(fruits_prices)
print('----------------\n')

fruits.__delitem__('apple') #usuwamy parę klucz-wartość
print(fruits.pop('banana')) #zabieramy samą wartość klucza
old_fruits = fruits.copy() # tworzymy kopię słownika
fruits.update(fruits2) # dodaje kolejną listę skrótow, takie same klucze uaktualnia a nowe dodaje
print(old_fruits)
print(fruits)
fruits.clear() # czyści cały słownik
print(fruits)

print('----------------\n')

# Przykład 1: Utworzenie słownika z listy kluczy
keys = ['a', 'b', 'c']
my_dict = dict.fromkeys(keys)
print(my_dict)
# Wynik: {'a': None, 'b': None, 'c': None}

# Przykład 2: Utworzenie słownika z listy kluczy i wartości domyślnych
default_value = 0
my_dict_with_defaults = dict.fromkeys(keys, default_value)
print(my_dict_with_defaults)
# Wynik: {'a': 0, 'b': 0, 'c': 0}

print('----------------\n')


phone_book = {}

phone_book['Norbert'] = "123-456-789"
phone_book['Madzia'] = "987-654-321"
phone_book['Abi'] = "123-987-456"
print(phone_book)

print(phone_book.get('Norbert')) #Zwraca wartość pod kluczem
print(phone_book.get('Janek')) #Zwraca wartość pod kluczem - jeżeli klucza nie ma to zwraca None

default_relation = None
relations = phone_book.fromkeys(phone_book, default_relation)
man = 'Chłopisko'
woman = 'Kobiecita'
dog = 'Psiak'
print(relations)
relations['Norbert'] = man
relations['Madzia'] = woman
relations['Abi'] = dog
print(relations)

# {klucz_wynikowy: wartość_wynikowa for element in sekwencja}
reverse_phone_book = {v: phone_book[k] for k, v in relations.items()}
print(reverse_phone_book)

print('\nponiżej krótko metoda setdefault()')
value_norbert = phone_book.setdefault('Norbert', '000-000-000') # W tym przypadku zwraca wartośc 'Norbert'
value_zbyszek = phone_book.setdefault('Zbyszek', '000-000-000') # W tym przypadu tworzy klucz Zbyszek z wartością obok(domyślną)
print(value_norbert)
print(phone_book.get('Zbyszek'))
print(value_zbyszek)

print('\n\n **** WYBORY *****\n')

voted_list = {}
voted_list['Michał'] = 'Tusk'
voted_list['Konrad'] = 'Kaczka'
voted_list['Zbych'] = None

#Proste użycie, jeżeli jest coś pod kluczem to znaczy że głos był już oddany. Złożoność stała !
def vote (voter,candidate):
    if voted_list.get(voter):
        print(f'Uciekaj {voter}, już głosowałeś')
    else:
        voted_list[voter] = candidate
        print(f'Gratulacje {voter}, Zagłosowałeś na {candidate}')

vote('Michał', 'Lepper')
vote('Zbych', 'Bidon')
vote('Zbych', 'Obama')

print('\n**** PO WYBORACH ****\n')