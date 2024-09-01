import logging

# Konfiguracja podstawowego logowania
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def przetwarzanie_danych(dane):
    logging.info('Rozpoczęcie przetwarzania danych')
    przefiltrowane_dane = [x for x in dane if x > 0]
    logging.info(f'Przefiltrowane dane: {przefiltrowane_dane}')

    suma = sum(przefiltrowane_dane)
    logging.info(f'Suma przefiltrowanych danych: {suma}')

    srednia = suma / len(przefiltrowane_dane) if przefiltrowane_dane else 0
    logging.info(f'Średnia przefiltrowanych danych: {srednia}')

    return srednia


# Wywołanie funkcji
wynik = przetwarzanie_danych([10, -5, 20, 0, 15])
