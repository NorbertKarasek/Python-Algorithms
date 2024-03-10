import random
import math

# Tworzenie tablicy z 10 losowymi liczbami
array = [random.randint(1, 50) for _ in range(10)]
print("Tablica wygenerowana losowo:", array)

# Liczenie liczby elementów większych niż 5
count_greater_than_5 = sum(1 for x in array if x > 5)
print("Liczba elementów większych niż 5:", count_greater_than_5)

# Obliczanie średniej arytmetycznej z elementów większych niż 5
sum_greater_than_5 = sum(x for x in array if x > 5)
average_greater_than_5 = sum_greater_than_5 / count_greater_than_5 if count_greater_than_5 > 0 else 0
print("Średnia arytmetyczna z elementów większych niż 5:", average_greater_than_5)

# Obliczanie średniej geometrycznej z elementów większych niż 5
product_greater_than_5 = math.prod(x for x in array if x > 5)
geometric_mean_greater_than_5 = product_greater_than_5 ** (1 / count_greater_than_5) if count_greater_than_5 > 0 else 0
print("Średnia geometryczna z elementów większych niż 5:", geometric_mean_greater_than_5)
# Sprawdzanie, które liczby są pierwsze w tablicy

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [x for x in array if is_prime(x)]
print("Liczby pierwsze w tablicy:", prime_numbers)
