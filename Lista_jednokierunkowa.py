# Implementacja wierzchołka
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# Implementacja listy
class LinkedList:
    def __init__(self):
        self.head = None

# Metoda dodania wierzchołka
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

# Metoda wyświetlania listy
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Metoda usuwania wierzchołka z warunkami
    def remove(self, data):
        current_node = self.head
        # Jeśli usuwamy pierwszy element listy
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev_node.next = current_node.next
        current_node = None


# Przykład użycia:
llist = LinkedList()
# Dodajemy elementy
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
# Usuwamy element
llist.remove(3)

# Wyświetlamy listę
print("Elementy listy jednokierunkowej:")
llist.display()
