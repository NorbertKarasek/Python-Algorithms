# implementacja grafu za pomocą listy sąsiedztwa
class Vertex:
    def __init__(self, key):
        self.key = key
        self.connections = {}

    def add_adj(self,vertex, weight=0):
        self.connections[vertex] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_weight(self, vertex):
        return self.connections[vertex]

    def __str__(self):
        return f'Zawartość key wierzchołka to {self.key}\njego połączenia to {self.connections}'

class Graph:
    def __init__(self):
        self.vertex_dict = {}

    def add_vertex(self,key):
        new_vertex = Vertex(key)
        self.vertex_dict[key] = new_vertex

    def get_vertex(self, key):
        if key in self.vertex_dict:
            return self.vertex_dict[key]
        return None

    def add_edge(self,f , t, weight=0):
        if f not in self.vertex_dict:
            self.add_vertex[f]
        if t not in self.vertex_dict:
            self.add_vertex(t)
        self.vertex_dict[f].add_adj(self.vertex_dict[t], weight)

myself = 'Norbert'
mylastname = 'Karasek'
myage = 28
myheight = 180
herself = 'Madzia'
herlastname = 'Jaborska'
herheight = 160

graph = Graph()
graph.add_vertex(myself)
graph.add_vertex(mylastname)
graph.add_vertex(myage)
graph.add_vertex(myheight)
graph.add_vertex(herself)

print(graph.vertex_dict)
graph.add_edge(myself, mylastname, 10)
graph.add_edge(myself, myage, 15)
graph.add_edge(myself, myheight, 20)
graph.add_edge(myself,herself, 100)
graph.add_edge(herself, myself, 100)
graph.add_edge(herself, herlastname, 10)
graph.add_edge(herself, herheight, 20)
graph.add_edge(herself, myage, 20)
print(graph.get_vertex(myself))

print('----------------------------\nMIASTA, POGODA, ODLEGŁOŚĆI\n')

class City:
    def __init__(self, city, temp):
        self.city = city
        self.temp = temp

    def __str__(self):
        return f'Miasto : {self.city}, temperatura : {self.temp}'



poznan = City('Poznań', '29 stopni')
wroclaw = City('Wrocław', '30 stopni')
lodz = City('Łódź', '15 stopni')
warszawa = City('Warszawa', '50 stopni')

graph_city = Graph()
graph_city.add_vertex(poznan)
graph_city.add_vertex(wroclaw)
graph_city.add_vertex(lodz)
graph_city.add_vertex(warszawa)

graph_city.add_edge(poznan, lodz, weight= 190)
graph_city.add_edge(lodz, poznan, weight= 190)
graph_city.add_edge(poznan, wroclaw, weight= 100)
graph_city.add_edge(wroclaw, poznan, weight=100)
graph_city.add_edge(wroclaw, lodz, weight= 230)
graph_city.add_edge(lodz, wroclaw, weight= 230)
graph_city.add_edge(lodz, warszawa, weight= 120)
graph_city.add_edge(warszawa, lodz, weight= 120)

print(graph_city.get_vertex(lodz))