print(bin(16))
print(bin(4))
print(bin(8))
print(bin(7))

print(1==1 and 2==2)#True
print(1==2 and 2==3)#False
print(1==1 and 2==4)#False
print(2 & 2) # zwraca 2 bo 0b10 & 0b10 = 0b10   bo 0&0=0-false  1&1=1 -True

print("-------------\n")

print(2 & 3) # to samo co niżej
print(0b10 & 0b11) # to samo co wyżej, zwraca 2 bo zwraca 0b10 bo 1 & 0 jest 0-false

print(10|11)

def is_even(n): #Sprawdza czy liczba jest parzysta 'even(ang.parzysta)'
    return not n & 1

print(is_even(5))

def is_power_of_2(n):     # sprawdza czy liczba n jest potęgą dwójki
    if n & (n-1) == 0:
        return True
    return False

print(is_power_of_2(8)) #true
print(is_power_of_2(10)) #false


def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(100)

print("----------\n")

def greatest_common_factor(n, m):
    if n<0 or m<0:
        raise ValueError("Liczby muszą być dodatnie!")
    if n == 0:
        return m
    if m == 0:
        return n

    if n>m:
        smaller = m
    else:
        smaller = n
    for divisor in range(1, smaller + 1):
        if (n % divisor == 0) and (m % divisor == 0):
            factor = divisor
    return factor

print(greatest_common_factor(24,12))
print(greatest_common_factor(100, 90))

print("\nTeraz to samo tylko wykrozystując algorytm euklidesa który ma złożoność logarytmiczną\n")

def euklides(x,y):
    if y == 0:
        x, y = y, x
    while y != 0:
        x,y = y, x % y
    return x

print(euklides(20,0))

print("------------\n")

def is_prime(n): # czy są liczbami pierwszymi, złożoność liniowa
    for i in range(2,n):
        if n % i ==0: # jeżeli podzielone przez którąkolwiek liczbę miedzy 2 a liczbą przed n, reszta będzie 0 to nie są pierwszymi
            return False
    return True

print(is_prime(5)) #True, jest pierwsza
print(is_prime(10)) #False, nie jest pierwsza
print(is_prime(42)) #True, jest pierwsza

print("----------")

import math

def is_prime_log(n): #złożoność logarytmiczna
    for i in range(2, int(math.sqrt(n) +1)): # wymienia liczby od 2 do Square Root(n) bo dla a * b = n, a i b jednocześnie nie mogą być większe od pierwiastka kwadratowego z n.
        if n % i == 0:
            return False
    return True

def find_primes(n): # pokaże listę liczb pierwszych od 2 do n
    return [i for i in range(2, n) if is_prime_log(i)]

print(find_primes(50))
