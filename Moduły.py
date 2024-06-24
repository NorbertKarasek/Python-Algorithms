import math
import random
import statistics
import time
import datetime
import keyword

# Moduł math

# Funkcja math.ceil() zwraca najmniejszą liczbę całkowitą większą od lub równą x.
print(math.ceil(1.4)) # 2
print(math.ceil(1.5)) # 2
print(math.ceil(2.1)) # 3

# Funkcja math.floor() zwraca największą liczbę całkowitą mniejszą od lub równą x.
print(math.floor(1.4)) # 1
print(math.floor(1.5)) # 1
print(math.floor(2.1)) # 2

# Funkcja math.fabs() zwraca wartość bezwzględną liczby x.
print(math.fabs(-1)) # 1.0
print(math.fabs(-1.5)) # 1.5
print(math.fabs(1.5)) # 1.5

# Funkcja math.factorial() zwraca silnię liczby x.
print(math.factorial(5)) # 120
print(math.factorial(6)) # 720

# Funkcja random.randint() zwraca losową liczbę całkowitą z zakresu od a do b.
print(random.randint(1, 10))

# Funkcja random.random() zwraca losową liczbę z zakresu od 0.0 do 1.0.
print(random.random())

# Funkcja statistics.mean() zwraca średnią arytmetyczną z listy.
print(statistics.mean([1, 2, 3, 4, 5])) # 3.0

# Funkcja statistics.median() zwraca medianę z listy.
print(statistics.median([10, 9, 8, 7, 6])) # 8.0

# Funkcja datetime.datetime.now() zwraca aktualną datę i godzinę.
print(datetime.datetime.now()) # 2021-02-02 12:00:00.000000
print(time.localtime()) # time.struct_time(tm_year=2021, tm_mon=2, tm_mday=2, tm_hour=12, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=33, tm_isdst=0)

now = datetime.datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_time) # 2021-02-02 12:00:00

# Funkcja keyword.kwlist zwraca listę słów kluczowych w Pythonie.
print(keyword.kwlist)
print(keyword.iskeyword("if")) # True
print(keyword.iskeyword("nauka")) # False
