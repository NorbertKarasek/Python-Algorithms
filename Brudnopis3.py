import heapq

graph = {'A': {'B': 2, 'C': 6}, 'B': {'D': 5}, 'C': {'D': 8}, 'D': {}}

#Brudnopis
distances = {vertex : float('infinity') for vertex in graph}
distances['A'] = 0
pq = [(0,'A')]
print(pq[0])
print(graph['A'].items())
abc = []
heapq.heappush(abc, (6,'C'))
heapq.heappush(abc, (2, 'B'))
heapq.heappush(abc, (3, 'D'))
heapq.heappush(abc, (1, 'Z'))# sortuje je dopiero gdy zachodzi relacja rodzic, dziecko, sąsiedzi nie muszą byc posortowani w kopiec minimalny
print(abc)
print(heapq.heappop(abc))
print(abc)