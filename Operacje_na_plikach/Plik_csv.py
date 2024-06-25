# Tworzenie pliku CSV
import csv  # Importuje moduł csv, który umożliwia pracę z plikami CSV (Comma-Separated Values)


# Otwiera plik 'Drugi_plik.csv' w trybie zapisu ('w') i ustawia zmienną csvfile jako odniesienie do tego pliku
# Użycie 'newline=''' eliminuje dodawanie dodatkowych pustych linii między wierszami w niektórych systemach operacyjnych

with open('D:Pyhton_notatki\Drugi_plik.csv', 'w', newline='') as csvfile:

    # Tworzy obiekt write, który będzie używany do zapisywania danych do pliku CSV
    # Ustawia delimiter na ',', co oznacza, że wartości będą rozdzielane przecinkami
    write = csv.writer(csvfile, delimiter=';')
    write.writerow(['Imię', 'Nazwisko', 'Wiek'])
    write.writerow(['Jan', 'Kowalski', '33'])
    write.writerow(['Anna', 'Nowak', '22'])
    write.writerow(['Piotr', 'Kowalczyk', '44'])

with open('D:Pyhton_notatki\Drugi_plik.csv', 'r') as csvfile:
    read = csv.reader(csvfile, delimiter=';')
    for row in read:
        print(row)

# Tworzenie pliku CSV za pomocą słowników

with open('D:Pyhton_notatki\Trzeci_plik.csv', 'w', newline='') as csvfile:
    headers = ['Imię', 'Nazwisko', 'Wiek', 'Płeć', 'Miasto', 'Kraj']
    writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=';')

    writer.writeheader()
    writer.writerow({'Imię': 'Jan', 'Nazwisko': 'Kowalski', 'Wiek': '33', 'Płeć': 'M', 'Miasto': 'Warszawa', 'Kraj': 'Polska'})
    writer.writerow({'Imię': 'Anna', 'Nazwisko': 'Nowak', 'Wiek': '22', 'Płeć': 'K', 'Miasto': 'Kraków', 'Kraj': 'Polska'})
    writer.writerow({'Imię': 'Piotr', 'Nazwisko': 'Kowalczyk', 'Wiek': '44', 'Płeć': 'M', 'Miasto': 'Gdańsk', 'Kraj': 'Polska'})
    writer.writerow({'Imię': 'Katarzyna', 'Nazwisko': 'Kowalska', 'Wiek': '55', 'Płeć': 'K', 'Miasto': 'Wrocław', 'Kraj': 'Polska'})
    writer.writerow({'Imię': 'Edyta', 'Nazwisko': 'Karasek', 'Wiek': '54', 'Płeć': 'K', 'Miasto': 'Łódź', 'Kraj': 'Polska'})

with open('D:Pyhton_notatki\Trzeci_plik.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        print(row['Imię'], row['Nazwisko'], row['Wiek'])