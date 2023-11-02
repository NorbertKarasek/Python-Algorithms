class Stack:
    def __init__(self):
        self.items = []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        self.items.pop()
    def size(self):
        return len(self.items)
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        return self.items[-1]

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def pop(self):
        if self.head is None:
            raise IndexError("Próbujesz zdjąć z pustego stosu")
        poppednode = self.head
        self.head = self.head.next
        return poppednode.data
    def look(self):
        print(f'pierwszy element stosu to - {(self.head.data)}')

stack = StackLinkedList()
stack.push(1)
stack.push(2)
stack.push(3)
stack.look()

for i in range(3):
    print(stack.pop())

#odwraca łańcuch znaków
word = "Siemaneczko"
print(word)
print(word[::-1])
print(''.join(reversed(word)))

def reversed_string(a_string):
    stack = []
    string = ''
    for c in a_string:
        stack.append(c)
    for c in a_string:
        string += stack.pop()
    return string
print(reversed_string("Norbert"))

#Wartość minimalna stosu

class MinStack():
    def __init__(self):
        self.main = []
        self.min = []

    def push(self,n):
        if len(self.main) == 0:
            self.min.append(n)
        elif n <= self.min[-1]:
            self.min.append(n)
        else:
            self.min.append(self.min[-1])
        self.main.append(n)

    def pop(self):
        self.min.pop()
        return self.main.pop()

    def get_min(self):
        return f'Wartość minimalna stosu to {self.min[-1]}'

    def __str__(self):
        return (str(self.main))

numbers1 = MinStack()
numbers1.push(2)
numbers1.push(4)
numbers1.push(1)
numbers1.push(5)
numbers1.push(8)
numbers1.push(9)

print(numbers1)
print(numbers1.min)
print(numbers1.get_min())
numbers1.pop()
print(numbers1.get_min())
numbers1.pop()
print(numbers1.get_min())
print(numbers1)

#tak sprawdzi czy jest tyle samo nawiasów zamykających co otwierających
def check_parentheses(a_string):
    parenthese1 = 0
    parenthese2 = 0
    for c in a_string:
        if c == ")":
            parenthese1 += 1
        elif c == "(":
            parenthese2 += 1
    if parenthese1 == parenthese2:
        return True
    return False

parenthese_string = ")( )("
print(check_parentheses(parenthese_string))

# tak czy każdy nawias otwierający ma swój zamykający

def check_closed_parentheses(a_string):
    stack = []
    for c in a_string:
        if c == "(" or c == "{":
            stack.append(c)
        if len(stack) != 0:
            if stack[-1] == "(" and c == "}":
                return False
            elif stack[-1] == "{" and c == ")":
                return False
        if c == ")" or c == "}":
            if len(stack) == 0:
                return False
            else:
               stack.pop()
    return len(stack) == 0

parenthese_string = ")()("
print(check_closed_parentheses(parenthese_string))
parenthese_string = "()(){}"
print(check_closed_parentheses(parenthese_string))

#Wartość maksymalna stosu

class MaxStack():
    def __init__(self):
        self.main = []
        self.max = []

    def push(self,n):
        if len(self.main) == 0:
            self.max.append(n)
        elif n >= self.max[-1]:
            self.max.append(n)
        else:
            self.max.append(self.max[-1])
        self.main.append(n)

    def pop(self):
        self.max.pop()
        return self.main.pop()

    def get_max(self):
        return f'Wartość maksymalna stosu to {self.max[-1]}'

    def __str__(self):
        return (str(self.main))

some_numbers = MaxStack()
some_numbers.push(4)
some_numbers.push(9)
some_numbers.push(4)
some_numbers.push(5)
some_numbers.push(7)
some_numbers.push(12)
print(some_numbers)
print(some_numbers.get_max())
some_numbers.pop()
print(some_numbers)
print(some_numbers.get_max())