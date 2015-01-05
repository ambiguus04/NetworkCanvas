class View(graph_tool.GraphWindow):

    white = [1,1,1,1]

    def draw(self, g):
        win = GraphWindow(g, g.pos, geometry=(800,600), vertex_text = g.txt, vertex_fill_color = self.white, vertex_halo = False, vertex_size = 20)

    def setTitle(self,title="nananna"):
        self.set_title(title)

    picked = None

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
        cid = GObject.idle_add(self.changeValues)
        self.connect("delete_event", Gtk.main_quit)
        self.show_all()
        Gtk.main()
