from NCModel import model
from NCView import view
import graph_tool as gt
class Controller:

    def __init__(self):
        g = model.Model()
        # gt.draw.graph_draw(g,g.pos)
        # a = g.createBA()
        win = view.View(g)
        win.setTitle("test")
        win.show()