from gi.repository import Gtk, Gdk, GdkPixbuf, GObject
import graph_tool as gt

class View(gt.draw.GraphWindow):

    white = [1,1,1,1]
    picked = None

    def __init__(self,m):
        gt.draw.GraphWindow.__init__(self, m.graph, m.pos, geometry=(800,600))


    def setTitle(self,title="nananna"):
        self.set_title(title)

    def changeValues(self):
        if self.graph.picked is not None and self.graph.picked is not False and self.graph.picked is not self.picked:
            if self.picked is not None:
                self.graph.txt[self.picked] = ""
            self.graph.txt[self.graph.picked] = str(int(self.graph.picked)) ## argh, adding commas!
            self.picked = self.graph.picked
        self.graph.regenerate_surface(lazy=False)
        self.graph.queue_draw()
        return True

    def show(self):
        # cid = GObject.idle_add(self.changeValues)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()
        Gtk.main()
