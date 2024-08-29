# Opis: Kolejki w Pythonie
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# implemenacja kolejki za pomocą listy
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class AQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self,item):
        self._size += 1
        node = Node(item)
        if self.rear is None:
            self.rear = node
            self.front = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndexError("próba pobrania z pustego elementu")
        self._size -= 1
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def size(self):
        return self._size

queue = AQueue()
queue.enqueue("BASIA")
queue.enqueue("KASIA")
queue.enqueue("ZOSIA")
queue.enqueue("JANEK")
queue.enqueue("WAŁEK")
print(queue.dequeue())
#poniżej czyścimy kolejkę
for i in range(queue.size()):
    print(queue.dequeue())

#Wbudowana klasa Queue Pythona:

from queue import Queue

q = Queue()
q.put('a')
q.put('b')
q.put('c')
print(f'Rozmiar kolejki q to {q.qsize()} elementy')

def queue_clean(a_queue):
    for i in range(a_queue.qsize()):
        a_queue.get()
    print(f'Kolejka została wyczyszczona, zostało {a_queue.qsize()} elementów')
queue_clean(q)

#Tworzenie kolejki przy użyciu dwóch stosów

class QueueStock:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self,item):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(item)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception("Kolejka nie może być pusta")
        return self.s1.pop()

    def __str__(self):
        return str(self.s1)

q1 = QueueStock()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print(q1)
q1.dequeue()
print(q1)

#Operacja dodawania elementu będzie złożoności O(1), zdejmowanie odwraca kolejki i zabiera z końca!

class QueueStock01:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def put(self,item):
        self.s1.append(item)

    def get(self):
        if len(self.s1) == 0:
            raise Exception('Nie ma nic w kolejce')
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        dequeued = self.s2.pop()
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
        return dequeued

    def __str__(self):
        return str(self.s1[::-1])

q2 = QueueStock01()
q2.put(1)
q2.put(2)
q2.put(3)
print(q2)
q2.get()
print(q2)
q2.get()
print(q2)
q2.get()

#Kolejka priorytetowa

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

    def __str__(self):
        return str(self.queue)