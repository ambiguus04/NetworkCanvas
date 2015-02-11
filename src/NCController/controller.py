from NCModel import model
from GView import window
import graph_tool as gt

class Controller:

    def __init__(self):
        self.m = model.Model()
        self.w = window.Window(self)
        self.w.show()

    def clicked_BA(self):
        self.m.create_BA()
        self.m.set_layout()
        self.w.add_graph(self.m)
        self.w.redraw()

    def clicked_ER(self):
        self.m.create_ER()
        self.m.set_layout()
        self.w.add_graph(self.m)
        self.w.redraw()

    def submitted_p(self, p):
        self.m.update_p(p)

    def submitted_N(self, N):
        self.m.update_N(N)

    def get_edges(self):
        return self.m.get_edges()