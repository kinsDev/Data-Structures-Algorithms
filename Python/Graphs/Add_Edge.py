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
        # if we want to connect two vertices v1 and v2 with an edge, we need to check whether they are present in the dictionary
        # if yes, it should add each other's adjacency list as new pages
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False


my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1, 2)

my_graph.print_graph()


"""
    EXPECTED OUTPUT:
    ----------------
    1 : [2]
    2 : [1]

"""


"""
Graph: Add Edge
Write a method called add_edge to the Graph class that adds a new edge between two vertices in the graph's adjacency list.

The method should take two parameters v1 and v2, which are the vertices that the edge should be added between. The method should first check that both vertices are present in the adj_list dictionary, and if they are, it should add both vertices to each other's adjacency list as new edges.

Specifically, the method should append v2 to the list of adjacent vertices for v1, and v1 to the list of adjacent vertices for v2. The method should then return True to indicate that the edge was successfully added to the graph.

If either v1 or v2 is not in the adj_list dictionary, the method should not add the edge and should return False to indicate that the edge was not added to the graph.
"""