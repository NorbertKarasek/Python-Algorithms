# Anagramy to łańcuchy zawierające te same litery, w obojętnie jakiej kolejnośći

def is_anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

s1 = '  pokorni'
s2 = 'okroPNI'
s3 = 'kabaczek'
s4 = 'inne słowo'

print(is_anagram(s1,s2))
print(is_anagram(s3,s4))

print("-----------\n")

print("monitor"[::-1]) #odwraca kolejność znaków w łańcuchu

def is_palindrom(word):
    if word.lower() == word[::-1].lower():
        return True
    return False

print(is_palindrom('zakaz'))
print(is_palindrom('kajak'))

print("--------")

print([letter for letter in 'samouk'])
print([letter for letter in 'samouk' if letter == 'c'])
print([letter for letter in 'samouk' if letter == 's'])
print([letter for letter in 'samouczek' if ord(letter) > 102]) #od 102 to w jezyku ASCII dalej od 'f' w alfabecie

represent_letter = 'a'
represent_number = '1'

print(represent_letter.isdigit()) # Tutaj isdigit() zwraca False ponieważ zmienna r..letter jest literą
print(represent_number.isdigit()) # isdigit() Zwraca True jeżeli wskażemy liczbę

s = 'Kup 2 w cenie 1'
n1 = [c for c in s if c.isdigit()] # tworzy listę samych numerów, używając funkcji pythona isdigit()
n2 = [c for c in s if c.isdigit()][-1]# ^^^ to samo plus wyświetla tylko ostatni element stworzonej listy
n3 = [c for c in s if not c.isdigit() and c != ' ']
print(s)
print(n1)
print(n2)
print(n3)

promotion = 'Kupcie 2 a 3 dostaniecie gratis, 5 nie ma '
numbers_inp_promotion = [element for element in promotion if element.isdigit()]
print(numbers_inp_promotion)
first_number_inpromotion = [element for element in promotion if element.isdigit()][0]
print(first_number_inpromotion)
last_number_inpromotion = [element for element in promotion if element.isdigit()][-1]
print(last_number_inpromotion)

print('------------\n')

#Szyfr Cezara

import string

print(string.ascii_lowercase) # wyświetla alfabet małych liter
print(string.ascii_uppercase) # wyświela alfabet dużych liter

def cipher(a_string, key):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypt = ''
    for c in a_string:
        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]
        else:
            encrypt += c
    return encrypt

print(cipher('Norbert Karasek', 3))

print('---------\n')

#wyzwanie
words_list = ['samouk', 'kod', 'pat', 'znak', 'programowanie', 'obiad', 'raz', 'dwa', ' kodowanie', 'co', 'trop']
longer_than_4letters = [word for word in words_list if len(word) > 4]

print(words_list)
print(longer_than_4letters)
