class Controller:

    def __init__(self):
        from NCModel import model
        from NCView import view
        g = model.Model()
        win = view.View()
        win.draw(g)
        win.setTitle("test")
        win.show()