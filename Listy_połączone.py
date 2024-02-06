print('Hello world\n\n')
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def search(self, target):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        if current.data == target:
            return True
        return False

    def remove(self,target):
        if self.head == target:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.next = current.next
            previous = current
            current = current.next
    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        current = previous

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except:
                return False

    def implement_cycle(self):
        first_node = self.head
        current = self.head
        while current.next:
            current = current.next
        current.next = first_node

    def __str__(self):
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return  str(nodes)


a_list = LinkedList()
a_list.append("Wtorek")
a_list.append("Środa")
a_list.append("Czwartek")
a_list.append("Piątek")
print(a_list)
print(a_list.search("Czwartek"))
a_list.remove("Czwartek")
print(a_list)
print(a_list.search("Czwartek"))

num_list = LinkedList()
for i in range(1,101):
    num_list.append(i)
print(num_list, end=" ")
print('')
num_list1 = LinkedList()
for i in range(1,101):
    num_list1.append(i)
print(num_list1, end=" ")
print('\n')
print(num_list.detect_cycle())
print(num_list1.detect_cycle())
num_list1.implement_cycle()
print(num_list.detect_cycle())
print(num_list1.detect_cycle())