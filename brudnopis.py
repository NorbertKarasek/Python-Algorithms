import array
an_array =array.array  ('i' ,(1,2,3,4,5,6,7,8,9,10))

for index, n in enumerate(an_array):
    print(f'[{index}] = {n}')
def even_odd(array_a):
    index_zero = 0
    for index,n in enumerate(array_a):
        if n  % 2 == 0:
            a = array_a[index_zero]
            array_a[index_zero] = n
            if index_zero != index:
                array_a[index] = a
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

class Fullname:
    def __init__(self, name, surname, balance, debet_accepted = None):
        self.name = name
        self.surname = surname
        self.balance = balance
        self.debet_accepted = debet_accepted

    def represent(self):
        print(f'Pełne imie i nazwisko = {self.name} {self.surname}')

    def show_balance(self):
        print(f'{self.name} ma {self.balance}PLN')

    def deposit(self, amount):
        self.balance+= amount
        print(f'{self.name} po wpłacie {amount} pln, masz teraz {self.balance}PLN')

    def withdraw(self, amount):
        if self.debet_accepted and (self.balance - amount) < 0:
            self.balance -= amount
            print(f'{self.name } UWAGA, zaciągasz dług ! Masz teraz {self.balance} pln.')
        else:
            if (self.balance - amount) < 0:
                print(f'{self.name} nie masz tyle pieniędzy')
                return
            else:
                self.balance -= amount
            print(f'{self.name} po wypłacie {amount} pln, masz teraz {self.balance}PLN')


    def boost(self):
        while self.balance < 2000:
            self.balance += 200
        print(f'{self.name} wyrównalismy twój stan konta do przynajmniej 2000zł')



name_one = Fullname('Norbert', 'Karasek', 1000, True)
name_two = Fullname('Zbyszek', 'Wałęsa', 2000, False)

print(name_one) # <__main__.Fullname object at 0x000001DB86916CD0> , Wskazuje że widzi obiekt w klasie Fullname w danym miejscu w komputerze
name_one.represent() # Pełne imie i nazwisko = Norbert Karasek , Używa funkcji która reprezentuje obiekt
print(name_two)# <__main__.Fullname object at 0x000001DB86916D10>
name_two.represent() # Pełne imie i nazwisko = Zbyszek Wałęsa
name_one.show_balance()
name_two.show_balance()
name_one.deposit(500)
name_two.withdraw(800)
name_two.withdraw(1300)
name_two.withdraw(800)
name_two.boost()
name_two.show_balance()
name_one.withdraw(3000)

head = None

if head:
    print("teraz nie napisze") # nie napisze nic bo head jest None / nie wykona instrukcji po if
if not head:
    print("teraz napisze ") # z użyciem not wykona insktrukcję, warunek if ponieważ not none = True

head = 10

if head: # jeżeli zmienna zawiera cokolwiek to wykonuje operację po if !!
    print("teraz napisze bo zmienna ma zawartość")
if not head:
    print("Teraz dopóki zmienna head nie będzie znowu None to nie wykona Print")

while head < 200:
    head += 10
    print(head)

print("-----------\n\n")
class Node:
    def __init__(self, data, next = None):
        self.data = data # dane, wartość, zmienna cokolwiek
        self.next = next# puste miejsce po elemencie, wskaźnik na kolejne

class LinkedList:
    def __init__(self):
        self.head = None # na wejściu mamy None

    def append(self,data): #np: a_list.append("wtorek")
        if not self.head: # na początku self.head jest None więc warunek się spełnia, wtorek staje się pierwszym obiektem klasy i ma wartość next = None
            self.head = Node(data)
            return # zwraca, kończy metodę append
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
#########TERAZ DALEJ, używamy znowu a_list.append("środa)
        def append(self, data):  # np: a_list.append("środa")
            if not self.head:  # teraz self.head ma to Node("wtorek", next = None) więc warunek if not nie spełnia się, omijamy
                self.head = Node(data) #omijamy
                return#omijamy
            current = self.head # ustalamy że current = self.head
            while current.next:  #current next teraz jest None, więc omijamy!
                current = current.next#omijamy
            current.next = Node(data)# ustalamy że current.next czyli next dla self.head to teraz Node("środa", next= None)
###########TERAZ DALEJ! Używamy a_list.append("czwartek")
            def append(self, data):  # np: a_list.append("czwartek")
                if not self.head: #self.head dalej jest Node("wtorek", z tym że next = Node("środa", next = None)  OMIJAMY BO COŚ JEST W SELF.HEAD
                    self.head = Node(data) #omijamy
                    return#omijamy
                current = self.head# current jest nadal self.head =  Node("wtorek", z tym że next = Node("środa", next = None)
                while current.next: #więc next z self.head COŚ MA WIĘC WYKONUJEMY Pętlę while.
                    current = current.next #ustalamy że current to next czyli Node("środa", next = None) wracamy do while i w tym momencie dla current.next jest NONE więc koniec pętli!!
                current.next = Node(data) #i ustalamy że ten next = None który skończył pętlę, jest teraz Node("czwartek", next = None)
                # i przy kolejnym użyciu metody append, zrobi to samo, przeleci całą listę aż next będzie None i ustawi go jaki obiekt klasy
                # Node gdzie będzie wartość podana w append("wartość") a next znowu będzie None!


import random
num_list = LinkedList()

for i in range(20):
    j = random.randint(0,30)
    num_list.append(j)
    print(j, end=" -> ") # end ustala jak ma kończyć pętlę zamiast przesuwać do następnej linijki

print(num_list.search(10))


print("--------\n")
from collections import deque # struktura danych używająca list połączonych

b_list = deque()
b_list.append("Harry")
b_list.append("Hermiona")
b_list.append("Ron")
print(b_list[1])
print(b_list[0])