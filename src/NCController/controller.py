from NCModel import model
from GView import window
import graph_tool as gt

class Controller:

    def __init__(self):
        self.w = window.Window(self)
        self.m = model.Model()
        self.w.show()

    def clicked_BA(self):
        self.m.createBA()
        self.m.setLayout()
        self.w.add_graph(self.m)
        self.w.redraw()

    def clicked_ER(self):
        pass