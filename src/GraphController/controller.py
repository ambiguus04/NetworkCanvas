class Controller:

    def __init__(self):
        g = GraphModel.Model()
        win = GraphView.View()
        win.draw(g)
        win.setTitle("test")
        win.show()