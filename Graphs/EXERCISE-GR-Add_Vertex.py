class Graph:
    def __init__(self):
        self.adj_list =  {}


    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    '''''ERASE FROM HERE UP!!!'''



    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

my_graph = Graph()

my_graph.add_vertex('A')
print(my_graph.add_vertex('A'))

my_graph.print_graph()



"""
    EXPECTED OUTPUT:
    ----------------
    A : []
    False

"""
