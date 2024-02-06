#Tablica jednowymiarowa
array = [1,2,3]

print(array[1]) # 2
print(array[0])

#Tablica wielowymiarowa
array = [[1,2,3], [4,5,6], [7,8,9]]
print(array[0][1])#2
print(array[1][1]) #5
print(array[2][0]) # 7

#Sortowanie listy, algorytm hybrydowy
names = ['Kamil Abencjusz', 'Norbert Karasek', 'Abel Zimbabwe', 'Kamelia Kabelo', 'Olimpia Szewczyk']
print(names)
print(sorted(names))

#TABLICE
import array

arr = array.array('f', (1.0, 1.5, 2.0, 2.5)) #'f' znacza float, tworzymy tablice jednorodną z wartosciami float

print(arr[0])
print(arr[1])


print('\n----------\n')
# funkcja enumerate
num_list = [10,20,30,40,50]

def index_contents(a_list):
    for index, n in enumerate(a_list):
        print(f'[{index}] = {n}')
        print(f'Wymienia jako pierwszy indeks :  {index}, i jako drugie zawartość elementu : {n}')

index_contents(num_list)

print('\n---------\n')

# Przesuwanie zer

def move_zeros(a_list):
    zero_index = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return(a_list)

x_list = [8,0,3,0,12]
move_zeros(x_list)
print(x_list) # [8, 3, 12, 0, 0]

print('\n---------\n')

#Łączenie list
films = ['Intersellar', 'Incepcja', 'Prestiż', 'Bezsenność', 'Batman: Początek']
ratings_list = [1,10,10,8,6]

films_ratings = list(zip(films, ratings_list))

print(films)
print(ratings_list)
print(films_ratings)

print('\n----------\n')

# Zbiór ang. SET , funkja python set()

a_set = set()
a_set.add('Kayne West')
a_set.add('Kendall Jenner')
a_set.add('Justin Bieber')

print(a_set)

a_set.add('Kayne West') # Do zbioru nie doda drugi raz tego samego !
print(a_set) # Wyświetli to smao co wyżej!

#Znajdowanie powtórzeń na listach

def return_dups(an_iterable): #zwracanie duplikatów
    dups = []
    a_set = set()

    for item in an_iterable: # mieli każdy element listy
        l1 = len(a_set) # sprawdza długośc zbioru przed dodaniem
        a_set.add(item) # dodaje element sprawdzanej listy
        l2 = len(a_set) # sprawdza dlugość zbioru po dodaniu
        if l1 == l2: # jeżeli dodało pomyślnie to leci do kolejnej pętli bo l1!=l2 a jeżli nie to długość się nie zmieni co oznacza że element jest juz w zbiorze
            dups.append(item) #i dodaje ten element do listy dups aby później móc wyświetlić duplikaty
    return dups

list_with_duplicates = ['Norbert', 'Norbert', 'Kamil', 'Michal', 'Janek', 'Kamil']

duplicates_of_list_above = return_dups(list_with_duplicates)
print(list_with_duplicates)
print(duplicates_of_list_above)

#Znajdowanie części wspólnych list

def return_shared(list1, list2):
    shared_elements = [i for i in list1 if i in list2]
    return shared_elements

a_list = [3,4,2,23,26,76,5]
b_list = [7,9,2,26,10,5]
shared_elements_of_above = return_shared(a_list, b_list)
print(a_list)
print(b_list)
print(shared_elements_of_above)

print('\n-----------\n')
# Przekształcanie na zbiory i wyszukanie wspolnych elementów w zbiorach
# ang. intersection - skrzyżowanie, set - zbiór
list_a = [1,2,3,4,5, 11]
list_b = [2,5,6,7,8,11]
list_c = [2,7,8,9,10, 11]

set_a = set(list_a)
set_b = set(list_b)
set_c = set(list_c)

print(set_a)
print(set_b)
print(set_c)
print (f" wspólne wartosci z 3 zbiorów = {(set_a.intersection(set_b,set_c))}") # funkcja szukania wspólnych elementów (skrzyżowań) dla zbiorów 'zbiór1.intersection(zbiór2)'

#zbiór można zmienić spowrotem na listę w prosty sposób

print(list(set_b.intersection(set_a))) # wyświetli to samo co wyżej ale jako listę

print('to samo tylko przy użyciu funkcji która robi to wszystko co u góry :)')
def return_inter(list1, list2, list3): # ten wariant porownuje 3 listy
    set_a = set(list1)
    set_b = set(list2)
    set_c = set(list3)
    return list(set_a.intersection(set_b, set_c))
print(return_inter(list_a, list_b, list_c))

#Wyzwanie even ang. parzyste | odd ang. nieparzyste
import array
an_array =array.array  ('i' ,(1,2,3,4,5,6,7,8,9,10))

for index, n in enumerate(an_array):
    print(f'[{index}] = {n}')
def even_odd(array_a):
    new_array = array.array('i', ())
    index_zero = 0
    for index,n in enumerate(array_a):
        if n  % 2 == 0:
            array_a[index_zero], array_a[index] = array_a[index], array_a[index_zero]
            index_zero += 1
    return array_a
print(even_odd(an_array))
def even_odd_sort(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    odd_numbers = [num for num in arr if num % 2 != 0]
    sorted_array = even_numbers + odd_numbers
    return sorted_array

input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorted_result = even_odd_sort(input_array)
print(sorted_result)