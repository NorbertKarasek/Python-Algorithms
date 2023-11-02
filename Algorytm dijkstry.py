import heapq

def dijkstra(graph, starting_vertex, chosen_vertex):
    distances = {vertex : float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    predecessors = {}
    pq = [(0, starting_vertex)]

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue


        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    shortest_path = []
    current = chosen_vertex
    while current:
        shortest_path.insert(0, current)
        current = predecessors.get(current)

    return distances[chosen_vertex], shortest_path

graph = {'A': {'B': 2, 'C': 6}, 'B': {'D': 5}, 'C': {'D': 8}, 'D': {}}

dijkstra(graph, 'A', 'D')
print(dijkstra(graph,'A','D'))