import graph_tool as gt
from numpy.random import *

class Model(gt.Graph):

    def __init__(self):
        gt.Graph.__init__(self, directed=False)
        self.N = 100
        self.random_graph(0.03)
        self.pos = gt.draw.sfdp_layout(self)

    def random_graph(self,p):
        for x in xrange(self.N):
            v = self.add_vertex()
        for x in xrange(self.N):
            for y in xrange(x):
                if (random() < p and x is not y):
                    self.add_edge(self.vertex(x), self.vertex(y))

    def createBA(self):
        self = gt.generation.price_network(self.N, directed=False)

    def setLayout(self, type = "sfdp"):
        if type == "sfdp":
            self.pos = gt.draw.sfdp_layout(self)

    def set_txt(self):
        self.txt = super.new_vertex_property("vector<string>")

    def clear_txt(self):
        for v in self.vertices():
            self.txt[v] = ""
