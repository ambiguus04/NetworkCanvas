import graph_tool as gt
from numpy.random import *

class Model():

    def __init__(self):
        self.graph = gt.Graph(directed=False)
        self.N = 100
        self.p = 0.1

    def random_graph(self):
        self.clear_graph()
        for x in xrange(self.N):
            v = self.graph.add_vertex()
        for x in xrange(self.N):
            for y in xrange(x):
                if (random() < self.p and x is not y):
                    self.graph.add_edge(self.graph.vertex(x), self.graph.vertex(y))

    def create_BA(self):
        self.clear_graph()
        self.graph = gt.generation.price_network(self.N, directed=False)

    def set_layout(self, type = "sfdp"):
        if type == "sfdp":
            self.pos = gt.draw.sfdp_layout(self.graph)

    def set_txt(self):
        self.txt = self.graph.new_vertex_property("vector<string>")

    def clear_txt(self):
        for v in self.graph.vertices():
            self.graph.txt[v] = ""

    def clear_graph(self):
        self.graph.clear()

    def create_ER(self):
        self.clear_graph()
        self.random_graph()

    def update_N(self, N = 100):
        self.N = N

    def update_p(self, p = 0.1):
        self.p = p

    def get_edges(self):
        return self.graph.edges()