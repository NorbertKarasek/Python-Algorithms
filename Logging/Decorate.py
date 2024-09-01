import logging
from functools import wraps

# Konfiguracja logowania
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def loguj_wejscie_i_wyjscie(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug(f'Wywołanie funkcji {func.__name__} z args: {args}, kwargs: {kwargs}')
        wynik = func(*args, **kwargs)
        logging.debug(f'Funkcja {func.__name__} zwróciła: {wynik}')
        return wynik
    return wrapper

@loguj_wejscie_i_wyjscie
def mnozenie(a, b):
    return a * b

@loguj_wejscie_i_wyjscie
def dodawanie(a, b):
    return a + b

@loguj_wejscie_i_wyjscie
def odejmowanie(a, b):
    return a - b

# Wywołanie funkcji
rezultat_mnozenie = mnozenie(6, 7)
rezultat_dodawanie = dodawanie(6, 7)
rezultat_odejmowanie = odejmowanie(6, 7)