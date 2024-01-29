import Algorytmy_wyszukiwania as Aw

# Sortowanie bąbelkowe

def bubble_sort(a_list):
    list_lenght = len(a_list) -1
    for i in range(list_lenght):
        no_swaps = True
        for j in range(list_lenght - i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j + 1], a_list[j]
                no_swaps = False
        if no_swaps:
            return a_list
    return a_list

numbers = [54,62,34,4,3,65,1]
print(numbers)

bubble_sort(numbers)
print(numbers)

print("---------")

def bubble_sort_byASCII(a_list):
    list_lenght = len(a_list) -1
    for i in range(list_lenght):
        no_swaps = True
        for j in range(list_lenght - i):
            if ord(a_list[j][0]) > ord(a_list[j+1][0]):
                a_list[j], a_list[j+1] = a_list[j + 1], a_list[j]
                no_swaps = False
        if no_swaps:
            return a_list
    return a_list

words = ['zbyszek', 'celina', 'barbara', 'adam']
print(words)
bubble_sort_byASCII(words)
print(words)

#Sortowanie poprzez wstawianie

def insertion_sort(a_list):
    for i in range(1,len(a_list)): # od pierwszego elementu do końca listy
        value = a_list[i] #ustawia value na aktualnie sprawdzany element
        while i > 0 and a_list[i-1] > value: #dopoki i>0 i poprzedni element listy jest wiekszy od sprawdzanego
            a_list[i] = a_list[i-1] #zamienia poprzedni element na sprawdzany
            i=i-1 #zmniejsza i o 1
        a_list[i] = value # i ustawia poprzedni element na ten co był sprawdzany
        #i jeżeli i dalej jest wieksze od 0 to powtarza pętle
    return a_list

numba = [6,5,8,2]
print(numba)
insertion_sort(numba)
print(numba)

#Sortowanie poprzez scalanie

def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        left_ind = 0
        right_ind = 0
        alist_ind = 0
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                a_list[alist_ind] = left_half[left_ind]
                left_ind += 1
            else:
                a_list[alist_ind] = right_half[right_ind]
                right_ind += 1
            alist_ind += 1

        while left_ind < len(left_half):
            a_list[alist_ind]=left_half[left_ind]
            left_ind += 1
            alist_ind +=1

        while right_ind < len(right_half):
            alist[alist_ind]=right_half[right_ind]
            right_ind +=1
            alist_ind +=1

print("----------\n")

numbers_1 = [56,75,22,31,4,6,90]
print(numbers_1)
print(sorted(numbers_1))

words_1 = ["Guido van Rossum", "James Gosling", "Brendan Eich", "Yukiro Matsumoto"]
print(words_1)
print(sorted(words_1))
print(sorted(words_1, reverse=True)) #ustawiamy reverse na True i dostajemy posortowane w odwrotnej kolejności
print(sorted(words_1, key=len)) # sortuje na podstawie klucza którym w tym przypadku jest len = długość stringa
#funkcja sorted() pokazuje posortowane a lista zostaje pierwotna.

print(numbers_1)
numbers_1.sort() # Funkcja .sort() sortuje na stałe !
print(numbers_1)
numbers_1.sort(reverse=True)
print(numbers_1)
words_1.sort(key=len)
print(words_1)

#Sortowanie szybkie

list_of_numbers = [10,5,2,3]
print(f"\n{list_of_numbers}")
def quicksort(a_list):
    if len(a_list) < 2:
        return a_list
    else:
        pivot = a_list[0]
        less = [i for i in a_list[1:] if i <= pivot]
        greater = [i for i in a_list[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print("Quicksort:")
print(quicksort(list_of_numbers))

#Przy pomocy Algorytmy_wyszukiwania.find_smallest() algorytmu można napisać sortowanie poprzez wybieranie.

def selection_sort(a_list):
    new_array = []
    for i in range (len(a_list)):
        smallest = Aw.find_smallest(a_list)
        new_array.append(a_list.pop(smallest))
    return new_array

print("SelectionSort:")
print(selection_sort(list_of_numbers))