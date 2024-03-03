# Pokrycie zbiorów
# * Przykładowe nadawanie sygnału przez stacje radiowe do określonych stanów *
# states_needed - Zbiór stanów do których chcemy nadawać
# stations - Słownik stacji (stacja : set(stany które obejmuje))

states_to_cover = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

stations = {
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'}
    }

# iteracja słowników w zbiorze
for station_example, states_for_station_example in stations.items():
    print('STACJA: ' + station_example.upper())
    print('OBSLGUJE STANY : ' + str(states_for_station_example))


# Podajemy do funkcji jakie stany potrzebujemy pokryć oraz stacje z ich stanami
def the_best_stations(states_needed, available_stations):
    final_stations = []
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in available_stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_needed -= states_covered
        final_stations.append(best_station)
    return final_stations

print('\n\n *** NAJLEPSZY WYBÓR STACJI DO NADAWANIA DO WYBRANYCH STANOW ***')
print(the_best_stations(states_to_cover, stations))