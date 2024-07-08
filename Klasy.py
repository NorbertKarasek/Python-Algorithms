# Klasy - definicje i obiekty

class Orange():  # Klasa
    def __init__(self, w, c):  # Metoda inicjalizacyjna, konstruktor, tu się tworzy obiekt
        self.weight = w
        self.color = c
        print("Utworzono!")  # Wyświetla się przy tworzeniu obiektu, inicjalizacji


or1 = Orange(10, "dark orange")  # Obiekt
or2 = Orange(8, "light orange")  # Obiekt
print(or1.weight)  # Wyświetla wartość wagi
print(or1.color)  # Wyświetla wartość koloru
or1.weight = 100  # Zmiana wartości wagi
or1.color = "light orange"  # Zmiana wartości koloru
print(or1.weight)
print(or1.color)
print(or2.weight)
print(or2.color)

print('-' * 30)


# Metody w klasach
class Dog():
    def __init__(self, name, age, owner=None):
        self.name = name
        self.age = age
        self.owner = None

    def bark(self):
        print("bark bark bark bark bark")


any_dog = Dog("Rex", 3)
print(any_dog.name)
print(any_dog.age)
any_dog.bark()


class Person():
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, my name is {}".format(self.name))


norbert = Person("Norbert")
norbert.introduce()

my_dog = Dog("Abi", 3, norbert)  # Przypisanie obiektu klasy Person do obiektu klasy Dog

print('-' * 30)


# Dziedziczenie

class Rectangle():
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.lenght = l
        self.recs.append((self.width, self.lenght))
        print("Shape created")

    def who_am_i(self):
        print("\nI am a rectangle")

    def print_size(self):
        print("{} by {}".format(self.width, self.lenght))

    def change_size(self, w, l):
        self.width = w
        self.lenght = l

    def area(self):
        return self.width * self.lenght

    def perimeter(self):
        return 2 * self.width + 2 * self.lenght


class Square(Rectangle):
    squares = []

    def __init__(self, wl):
        super().__init__(wl, wl)
        self.squares.append((self.width, self.lenght))
        print("Square created")

    def who_am_i(self):
        print("\nI am a square")

    def change_size(self, size):
        self.width = size
        self.lenght = size


# rectangle
a_rectangle = Rectangle(20, 30)
a_rectangle.who_am_i()
a_rectangle.print_size()
print(a_rectangle.area())
print(a_rectangle.perimeter())
a_rectangle.change_size(30, 40)
a_rectangle.print_size()
print(a_rectangle.perimeter())

# square
a_square = Square(20)
a_square.who_am_i()
a_square.print_size()
print(a_square.area())
print(a_square.perimeter())
a_square.change_size(30)
a_square.print_size()
print(a_square.perimeter())

print(Rectangle.recs)
print(Square.squares)

print('-' * 30)


class Lion():
    def __init__(self, name):
        self.name = name


lion = Lion("Dilbert")
print(lion)  # Wyświetla adres obiektu w pamięci
print(lion.name)  # Wyświetla wartość atrybutu name


class Tiger():
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # Metoda specjalna, nadpisuje domyślną reprezentację obiektu
        return self.name


tiger = Tiger("Albert")
print(tiger)  # Wyświetla wartość atrybutu name

print('-' * 30)


class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):  # Metoda specjalna, nadpisuje domyślny operator dodawania
        return abs(self.n + other.n)


x = AlwaysPositive(-20)
y = AlwaysPositive(10)
print(x + y)  # Wyświetla 10, bez metody __add__ nie pozwoli dodać elementów klasy.

print('-' * 30)


class Person:
    def __init__(self):
        self.name = 'Bob'


bob = Person()
another_bob = Person()
same_bob = bob
print(bob is same_bob)  # True - obie zmienne wskazują na ten sam obiekt
print(bob is another_bob)  # False - tak samo jak w przypadku liczb czy stringów -  2 = int i 3 = int, ale 2 != 3
