from gi.repository import Gtk, Gdk, GdkPixbuf, GObject
import graph_tool as gt

class View(gt.draw.GraphWidget):

    white = [1,1,1,1]
    picked = None

    def __init__(self, m):
        gt.draw.GraphWidget.__init__(self, m.graph, m.pos)
