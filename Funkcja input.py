class Name:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def presentation(self):
        print(f' Hi my name is: {self.name} and my surname is: {self.surname}')

first_move = input('Please enter your name: ')
second_move = input('Please enter your Surname: ')

user1 = Name(first_move, second_move)
user1.presentation()

a = input('first number: ')
b = input('second number: ')
print(int(a) + int(b))


print('\nTworzenie postaci')
name = input('Podaj imię bohatera: ')
surname = input('Podaj nazwisko bohatera: ')
age = input('Podaj wiek bohatera: ')
character = {}
character['Name'] = name
character['Surname'] = surname
character['Age'] = age
print(character)