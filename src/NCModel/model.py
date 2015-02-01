import graph_tool as gt
from numpy.random import *

class Model():

    def __init__(self):
        self.graph = gt.Graph(directed=False)
        self.N = 100

    def random_graph(self, p):
        for x in xrange(self.N):
            v = self.graph.add_vertex()
        for x in xrange(self.N):
            for y in xrange(x):
                if (random() < p and x is not y):
                    self.graph.add_edge(self.graph.vertex(x), self.graph.vertex(y))

    def createBA(self):
        self.graph = gt.generation.price_network(self.N, directed=False)

    def setLayout(self, type = "sfdp"):
        if type == "sfdp":
            self.pos = gt.draw.sfdp_layout(self.graph)

    def set_txt(self):
        self.txt = self.graph.new_vertex_property("vector<string>")

    def clear_txt(self):
        for v in self.graph.vertices():
            self.graph.txt[v] = ""
