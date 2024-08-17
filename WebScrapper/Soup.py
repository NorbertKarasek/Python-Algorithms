import urllib.request
from bs4 import BeautifulSoup
import os


class Scraper:
    def __init__(self,site):
        self.site = site


    def scrape(self):
        r = urllib.request.urlopen(self.site) # otwarcie strony - zwraca obiekt html
        html = r.read() # odczytanie zawartości strony - zwraca kod html
        parser = "html.parser" # parser html
        sp = BeautifulSoup(html,parser) # przekazanie kodu html do obiektu BeautifulSoup
        path = os.path.join('D:', 'Pyhton_notatki', 'Linki_z_.txt') # ścieżka do pliku - tworzy lub edytuje plik
        write_urls = open(path, 'a') # otwarcie pliku w trybie 'a' - append
        for tag in sp.find_all("a"): # wyszukanie wszystkich tagów 'a' - linków
            url = tag.get("href") # pobranie linku
            if url is None: # jeżeli link jest pusty, to pomiń
                continue
            if "html" in url: # jeżeli link zawiera 'html', to zapisz go do pliku
                write_urls.write("\n" + url) # zapisanie linku do pliku
        write_urls.close() # zamknięcie pliku


news = "https://www.wp.pl/" # strona, z której będą pobierane linki
first_search = Scraper(news) # utworzenie obiektu klasy Scraper
first_search.scrape() # wywołanie metody scrape() na obiek