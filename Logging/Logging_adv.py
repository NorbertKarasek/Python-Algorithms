import logging
from logging.handlers import RotatingFileHandler

# Tworzenie loggera
logger = logging.getLogger('moja_aplikacja')
logger.setLevel(logging.DEBUG)

# Tworzenie handlera do pliku z rotacją
file_handler = RotatingFileHandler('aplikacja.log', maxBytes=1000000, backupCount=5)
file_handler.setLevel(logging.DEBUG)

# Tworzenie handlera do konsoli
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Tworzenie formatu logów
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Dodanie handlerów do loggera
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def funkcja_przykladowa(x, y):
    logger.info('Funkcja funkcja_przykladowa została wywołana')
    wynik = x + y
    logger.debug(f'Obliczanie wyniku: {x} + {y} = {wynik}')
    return wynik

# Wywołanie funkcji
rezultat = funkcja_przykladowa(40, 50)
