from gi.repository import Gtk, Gdk
from NCView import view
# from NCController import controller

class Window(Gtk.Window):

    def __init__(self, controller):
        self.controller = controller
        Gtk.Window.__init__(self, title="Network Canvas")
        self.set_default_size(900, 600)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.table = Gtk.Table(12, 6, True)
        self.grid = Gtk.Table(1, 2, True) #main grid: left - buttons in table, right - drawing area
        self.add(self.grid)
        self.grid.attach(self.table, 0, 1, 0, 1)
        self.create_btns()
        self.clear_drawing_area()

    def create_btns(self):
        self.create_btn_BA()
        self.create_btn_ER()

    def create_btn_BA(self):
        self.btnBA = Gtk.Button(label="BA network")
        self.btnBA.connect("clicked", self.on_BA_clicked)
        self.table.attach(self.btnBA, 1, 2, 1, 2)

    def create_btn_ER(self):
        self.btnER = Gtk.Button(label="ER network")
        self.btnER.connect("clicked", self.on_ER_clicked)
        self.table.attach(self.btnER, 2, 3, 1, 2)

    def on_BA_clicked(self, btn):
        self.controller.clicked_BA()

    def on_ER_clicked(self, btn):
        self.controller.clicked_ER()

    def add_graph(self, m):
        self.da = view.View(m)
        self.grid.attach(self.da, 1, 2, 0, 1)


    def clear_drawing_area(self):
        self.da = Gtk.DrawingArea()
        color = Gdk.color_parse("#ffffff")
        rgba = Gdk.RGBA.from_color(color)
        self.da.override_background_color(0, rgba)
        self.grid.attach(self.da, 1, 2, 0, 1)

    def show(self):
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        Gtk.main()

    def redraw(self):
        self.show_all()
