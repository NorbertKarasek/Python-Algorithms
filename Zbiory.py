# Struktura danych
# Nie zawiera duplikatów

fruits = {'awokado', 'banan', 'pomidor'}  # set
vegetables = {'marchew', 'seler', 'pomidor'}  # set
fruits1 = {'awokado': 2.34, 'banan': 2.22}  # dict

print(fruits, type(fruits))
print(vegetables, type(vegetables))
print(fruits1, type(fruits1))

print('\nSUMA ZBIORÓW')
fruits_plus_vegetables = fruits | vegetables
print(fruits_plus_vegetables)

print('\nRÓŻNICA ZBIORÓW')  # odejmuje elementy vegetables od fruits
fruits_minus_vegetables = fruits - vegetables
print(fruits_minus_vegetables)

print('\nELEMENTY WSPÓLNE ZBIORÓW')
in_fruits_and_vegetables = fruits & vegetables
print(in_fruits_and_vegetables)