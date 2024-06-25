import pandas as pd
from openpyxl import load_workbook

# Odczytuje dane z pliku Excel
my_file = pd.read_excel('D:Pyhton_notatki\Pandas_poczatki.xlsx', sheet_name='Arkusz1')

# Manipulacja danymi (dodaje nowe kolumny)
my_file['Pelne Imie'] = my_file['Imie'] + ' ' + my_file['Nazwisko']
my_file['Kraj'] = 'Polska'

# Dodaje dodatkowe dwie osoby
additional_data = pd.DataFrame({
    'Imie': ['Katarzyna', 'Marek'],
    'Nazwisko': ['Zielinska', 'Nowicki'],
    'Wiek': [29, 34],
    'Plec': ['K', 'M'],
    'Pelne Imie': ['Katarzyna Zielinska', 'Marek Nowicki'],
    'Kraj': ['Polska', 'Polska']
})

# Dodaje nowe osoby do DataFrame
my_file = pd.concat([my_file, additional_data], ignore_index=True)

# Zmienia nazwy kolumn
my_file = my_file.rename(columns={'Pelne Imie': 'Imie i Nazwisko'})

# Zmienia kolejność kolumn
my_file = my_file[['Imie i Nazwisko', 'Imie', 'Nazwisko', 'Wiek', 'Plec', 'Kraj']]

# Usuwa pojedyncze kolumny Imie i Nazwisko
my_file = my_file.drop(columns=['Imie', 'Nazwisko'])

# Zapisuje dane do pliku CSV i Excel
my_file.to_csv('D:Pyhton_notatki\csv_by_python.csv', sep=';', index=False)
my_file.to_excel('D:Pyhton_notatki\excel_by_python.xlsx', index=False)

# Odczytuje dane z pliku CSV
my_csv = pd.read_csv('D:Pyhton_notatki\csv_by_python.csv', delimiter=';')
my_excel = pd.read_excel('D:Pyhton_notatki\excel_by_python.xlsx')

# Wyświetla dane
print(my_csv)
print('')
print(my_excel)
