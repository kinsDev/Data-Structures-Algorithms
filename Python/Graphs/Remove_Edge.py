class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        v_list = []
        for vertex in self.adj_list:
            v_list.append(vertex)
        v_list.sort()
        for v in v_list:
            print(v, ':', self.adj_list[v])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

# I added the try and catch error method so incase I am advised to remove an edge between two vertices that are not connected
# I can ignore that error and still print the resulting graph


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')

print('Graph before remove_edge():')
my_graph.print_graph()


my_graph.remove_edge('A', 'C')


print('\nGraph after remove_edge():')
my_graph.print_graph()


"""
    EXPECTED OUTPUT:
    ----------------
    Graph before remove_edge():
    A : ['B', 'C']
    B : ['A', 'C']
    C : ['B', 'A']

    Graph after remove_edge():
    A : ['B']
    B : ['A', 'C']
    C : ['B']
    
"""


"""
Graph: Remove Edge
Write a method called remove_edge that removes an edge between two vertices in the graph's adjacency list.

The method should take two parameters v1 and v2, which are the vertices that the edge should be removed between.

The method should first check that both vertices are present in the adj_list dictionary, and if they are, it should remove the edge between them.
"""