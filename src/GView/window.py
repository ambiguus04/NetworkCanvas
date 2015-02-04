from gi.repository import Gtk, Gdk
from NCView import view

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Network Canvas")

        self.set_default_size(900,600)
        # self.set_resizable(False)
        self.set_position(Gtk.WindowPosition.CENTER)
        # self.set_border_width(10)
        self.table = Gtk.Table(12,12,True)
        # self.table.set_col_spacings(10)
        # self.table.set_row_spacings(10)
        self.add(self.table)
        btn = []
        btn.append(Gtk.Button(label="Button 1"))
        btn.append(Gtk.Button(label="Button 2"))
        btn.append(Gtk.Button(label="Button 3"))
        btn.append(Gtk.Button(label="Button 4"))
        # da = Gtk.DrawingArea()
        # da.override_background_color(0,)
        # self.table.attach(da,6,12,0,12)
        for i in range(0,4):
            self.table.attach(btn[i],i,i+1,0,1)

    def on_button_clicked(self, widget):
        print("heelllo")

    def add_graph(self, m):
        graph = view.View(m)
        graph.set_size_request(400,300)
        self.table.attach(graph,6,12,0,12)


    def show(self):
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        Gtk.main()
