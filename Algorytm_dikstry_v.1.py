# Inny sposób implementacji algorytmu Dijkstry

# Budujemy symbolicznego grafa - graphA #
# Budujemy tablicę skrótów kosztu dotarcia do jego wierzchołków #
# podając koszt dotarcia tylko do pierwszych, reszta jako infinity #
# Budujemy tablicę skrótów rodziców kolejnych wierzchołków #
# podając tylko rodziców pierwszych wierzchołków, reszta jako None #

# WSZYSTKO BĘDZIE SIĘ AKUTUALIZOWAĆ PODCZAS WYKONIANIA ALGORYTMU #

graphA = {'start': {}}
graphA['start']['A'] = 6
graphA['start']['B'] = 2

graphA['A'] = {}
graphA['A']['meta'] = 1

graphA['B'] = {}
graphA['B']['A'] = 3
graphA['B']['meta'] = 5

graphA['meta'] = {}

# kilka wyświetleń
print(graphA['start'].keys())  # wyświetlimy jego sąsiadów, czyli jest on połączony krawędziami z tymi wierzchołkami
print(graphA['start']['A'])  # waga krawędzi do wierzchołka A
print(graphA['start']['B'])
print('-------------------\n')

# Tablica skrótów z kosztami przechodzenia po wierzchołkach
infinity = float('inf')  # oznacza nieskończoność
costs_of_graphA_edges = {'A': 6, 'B': 2, 'meta': infinity}

# Tabela skrótów dla rodziców ('A'-wierzchołek : 'rodzic')
parents_of_graph_vertices = {'A': 'start', 'B': 'start', 'meta': None}


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
    print(f'najmniejsze koszty dotarcia do wierzchołków {costs}')
    print(f'najtańsza droga którą musi podążyc aby otrzymać takie koszta (do tego wierzchołka : tą drogą){parents}')
    return costs, parents


dijkstra(graphA, costs_of_graphA_edges, parents_of_graph_vertices)
