class Model(graph_tool.Graph):

    N = 100

    def createBA(self):
        self = price_network(self.N, directed=False)

    def setLayout(self, type = "sfdp"):
        if type == "sfdp":
            self.pos = sfdp_layout(self)

    def setTxt(self):
        self.txt = super.new_vertex_property("vector<string>")

    def clearTxt(self):
        for v in self.vertices():
            self.txt[v] = ""
