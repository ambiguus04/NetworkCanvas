from NCModel import model
from NCView import view
from GView import window
import graph_tool as gt
class Controller:

    def __init__(self):
        w = window.Window()
        m = model.Model()
        # m.random_graph(0.2)
        m.createBA()
        m.setLayout()
        # gt.draw.graph_draw(g,g.pos)
        # a = g.createBA()
        # win = view.View(m)
        w.add_graph(m)
        w.show()
        # win.setTitle("test")
        # win.show()