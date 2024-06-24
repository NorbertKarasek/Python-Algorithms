import os

path = os.path.join('D:','Pyhton_notatki','Pierwszy_plik.txt')
print(path)

# Funkcja os.path.exists() zwraca True, jeżeli plik istnieje, w przeciwnym wypadku False.
print(os.path.exists(path)) # False

lets_create = open(path, 'w')
lets_create.write(
'''
Pierwszy plik
Pierwsza linijka
Druga linijka
Można tak długo...
'''
)
lets_create.close()

print(os.path.exists(path)) # True
### Jeżeli odpalimy ten skrypt, to w katalogu D:\Python_notatki zostanie utworzony plik Pierwszy_plik.txt
### za drugim razem będzie nadpisywał plik, bo jest otwarty w trybie 'w'.
### Aby nie nadpisywać pliku, trzeba otworzyć go w trybie 'a' (append).

lets_create = open(path, 'a')
lets_create.write(
''' \nTeraz będziemy pisać na końcu pliku. ''')
lets_create.close()

lets_create = open(path, 'r')
file_content = lets_create.read()
lets_create.close()
print(f'Oto odczytana zawartość pliku : \n {file_content}')

# Instrukcją with można otworzyć plik, a po wyjściu z bloku with plik zostanie automatycznie zamknięty. W innym przypadku trzeba pamiętać o zamknięciu pliku.
with open(path, 'a') as lets_write_more:
    file_content = lets_write_more.write("""\nTeraz będziemy pisać jeszcze więcej na końcu pliku.""")