#Wyszukiwanie liniowe

def linear_search(a_list, n):
    for i in a_list:
        if i == n:
            return True
    return False

a_list = [1,8,32,91,5,15,9,100,3]

print(linear_search(a_list, 91))
print(91 in a_list)
print('a' in 'automatyzacja')

print("-----------\n")

#Wyszukiwanie najmniejszej liczby

b_list = [8,32,91,5,1,15,9,100,3]
def find_smallest(a_list):
    smallest = a_list[0]
    smallest_index = 0
    for i in range (1, len(a_list)):
        if a_list[i] < smallest:
            smallest = a_list[i]
            smallest_index = i
    #print(f"Najmniejsza liczba w tablicy to: {smallest}")
    #print(f"Jest na indeksie: [{smallest_index}]")
    return smallest_index

find_smallest(b_list)

print("-----------\n")

sorted_list = [11,12,13,14,15,16,17,18,19,20]

def binary_search(list, n):
    first = 0
    last = len(list) - 1
    while last >= first:
        mid = (first + last) // 2
        if list[mid] == n:
            return True
        else:
            if n < list[mid]:
                last = mid -1
            else:
                first = mid + 1
    return False

print(binary_search(sorted_list, 12))

print("---------------")

#Wyszuiwanie binarne

from bisect import bisect_left


sorted_fruits = ['ananas', 'banan', 'kiwi', 'mango', 'winogrona']
print(bisect_left(sorted_fruits, 'banan'))
print(bisect_left(sorted_fruits, 'winogrona'))
print(bisect_left(sorted_fruits, 'bataty'))

def binary_search_module(list, target):
    index = bisect_left(list, target)
    if index <= len(list) and list[index] == target:
        return True
    return False

print(binary_search_module(sorted_fruits, 'banan'))
print(binary_search_module(sorted_fruits, 'bataty'))

print(ord('a'))

print("-------------")


sorted_letters = ['a','b','c','d','e','f','g']

def binary_search_byASCII(list, n):
    first = 0
    last = len(list) - 1
    while last >= first:
        mid = (first + last) // 2
        if ord(list[mid]) == ord(n):
            return True
        else:
            if ord(n) < ord(list[mid]):
                last = mid -1
            else:
                first = mid + 1
    return False

print(binary_search_byASCII(sorted_letters, 'b'))

print("-----------")
