fruits = {'banana': 1.76,
          'apple': 4.23,
          'strawberry': 2.25,
          'pineapple': 7.70}

fruits_keys = fruits.keys() #zwraca same klucze słownika
print(fruits_keys)
fruits_viev = fruits.items() #zwraca listę tupli[(klucz, wartość)] które są zawartością słownika fruits []-lista ()-tuple
print(fruits_viev)

fruits_list = []
fruits_prices = []
for fruit, price in fruits_viev:
    fruits_list.append(fruit)
    fruits_prices.append(price)

print(fruits_list)
print(fruits_prices)
print(fruits['banana'])
print(fruits['apple'])