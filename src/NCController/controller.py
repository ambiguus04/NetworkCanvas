from NCModel import model
from NCView import view
import graph_tool as gt
class Controller:

    def __init__(self):
        m = model.Model()
        # m.random_graph(0.2)
        m.createBA()
        m.setLayout()
        # gt.draw.graph_draw(g,g.pos)
        # a = g.createBA()
        win = view.View(m)
        win.setTitle("test")
        win.show()