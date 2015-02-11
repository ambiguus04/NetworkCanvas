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
        self.create_spin_p()
        self.create_spin_N()

    def create_btn_BA(self):
        self.btn_BA = Gtk.Button(label="BA network")
        self.btn_BA.connect("clicked", self.on_BA_clicked)
        self.table.attach(self.btn_BA, 1, 2, 1, 2)

    def create_btn_ER(self):
        self.btn_ER = Gtk.Button(label="ER network")
        self.btn_ER.connect("clicked", self.on_ER_clicked)
        self.table.attach(self.btn_ER, 2, 3, 1, 2)

    def create_spin_p(self):
        self.label_p = Gtk.Label("p: ")
        self.spin_p = Gtk.SpinButton(digits = 2)
        self.spin_p.set_numeric(True)
        self.spin_p.set_range(0, 1)
        self.spin_p.set_increments(0.01, 0.01)
        self.table.attach(self.label_p, 1, 2, 2, 3)
        self.table.attach(self.spin_p, 2, 3, 2, 3)
        self.spin_p.set_value(0.1)

    def create_spin_N(self):
        self.label_N = Gtk.Label("N (vertices): ")
        self.spin_N = Gtk.SpinButton()
        self.spin_N.set_numeric(True)
        self.spin_N.set_increments(1, 1)
        self.spin_N.set_range(0, 1000)
        self.table.attach(self.label_N, 1, 2, 3, 4)
        self.table.attach(self.spin_N, 2, 3, 3, 4)
        self.spin_N.set_value(100)

    def on_BA_clicked(self, btn):
        self.submit_params()
        self.controller.clicked_BA()


    def on_ER_clicked(self, btn):
        self.submit_params()
        self.controller.clicked_ER()

    def submit_params(self):
        self.controller.submitted_p(self.spin_p.get_value())
        self.controller.submitted_N(self.spin_N.get_value_as_int())

    def create_vertices_list(self):
        self.vertices_list = Gtk.ListStore(int, int)
        for e in self.controller.get_edges():
            self.vertices_list.append(list(e))
        self.current_filter = None
        self.v1_filter = self.vertices_list.filter_new()
        self.v1_filter.set_visible_func(self.v1_filter_func)
        self.treeview = Gtk.TreeView.new_with_model(self.v1_filter)
        for i, column_title in enumerate(["vertex", "vertex"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)
        self.scroll_treelist = Gtk.ScrolledWindow()
        self.scroll_treelist.set_vexpand(True)
        self.table.attach(self.scroll_treelist, 1, 3, 4, 11)
        self.scroll_treelist.add(self.treeview)
        self.show_all()

    def v1_filter_func(self, model, iter, data):
        if self.current_filter is None or self.current_filter == "None":
            return True
        else:
            return model[iter][2] == self.current_filter


    def add_graph(self, m):
        self.da = view.View(m)
        self.grid.attach(self.da, 1, 2, 0, 1)
        self.create_vertices_list()


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
