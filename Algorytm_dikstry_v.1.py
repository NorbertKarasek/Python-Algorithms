# Inny sposób implementacji algorytmu Dijkstry

# Budujemy symbolicznego grafa - graphA #
# Budujemy tablicę skrótów kosztu dotarcia do jego wierzchołków #
# podając koszt dotarcia tylko do pierwszych, reszta jako infinity #
# Budujemy tablicę skrótów rodziców kolejnych wierzchołków #
# podając tylko rodziców pierwszych wierzchołków, reszta jako None #

# WSZYSTKO BĘDZIE SIĘ AKUTUALIZOWAĆ PODCZAS WYKONIANIA ALGORYTMU #

graphA = {'start': {}}
graphA['start']['A'] = 5
graphA['start']['B'] = 2

graphA['A'] = {}
graphA['A']['D'] = 2
graphA['A']['C'] = 4

graphA['B'] = {}
graphA['B']['A'] = 8
graphA['B']['D'] = 7

graphA['C'] = {}
graphA['C']['D'] = 6
graphA['C']['E'] = 3
graphA['C']['F'] = 2

graphA['D'] = {}
graphA['D']['E'] = 5

graphA['E'] = {}
graphA['E']['F'] = 2
graphA['E']['meta'] = 200

graphA['F'] = {}
graphA['F']['G'] = 4
graphA['F']['H'] = 5
graphA['F']['meta'] = 32

graphA['G'] = {}
graphA['G']['H'] = 2
graphA['G']['I'] = 1

graphA['H'] = {}
graphA['H']['I'] = 5
graphA['H']['I'] = 1

graphA['I'] = {}
graphA['I']['meta'] = 1

graphA['meta'] = {}

# kilka wyświetleń
print(graphA['start'].keys())  # wyświetlimy jego sąsiadów, czyli jest on połączony krawędziami z tymi wierzchołkami
print(graphA['start']['A'])  # waga krawędzi do wierzchołka A
print(graphA['start']['B'])
print('-------------------\n')

# Tablica skrótów z kosztami przechodzenia po wierzchołkach
infinity = float('inf')  # oznacza nieskończoność
costs_of_graphA_edges = {'A': 5,
                         'B': 2,
                         'C': infinity,
                         'D': infinity,
                         'E': infinity,
                         'F': infinity,
                         'G': infinity,
                         'H': infinity,
                         'I': infinity,
                         'meta': infinity}

# Tabela skrótów dla rodziców ('A'-wierzchołek : 'rodzic')
parents_of_graph_vertices = {'A': 'start',
                             'B': 'start',
                             'C': None,
                             'D': None,
                             'E': None,
                             'F': None,
                             'G': None,
                             'H': None,
                             'I': None,
                             'meta': None}


def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(graph, costs, parents):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n, weight in neighbors.items():
            new_cost = cost + weight
            if new_cost < costs.get(n, float('inf')):
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    # Znajdź najkrótszą ścieżkę
    shortest_path = ['meta']
    while parents[shortest_path[-1]] != 'start':
        shortest_path.append(parents[shortest_path[-1]])
    shortest_path.append('start')
    shortest_path.reverse()
    print(f'Najmniejsze koszty dotarcia do wierzchołków {costs}')
    print(f'Rodzice najkrótszych scieżek do wierzchołków {parents}')
    print('Najkrótsza scieżka', shortest_path)
    return shortest_path


dijkstra(graphA, costs_of_graphA_edges, parents_of_graph_vertices)
