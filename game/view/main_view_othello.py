from view.grid_view import GridView


class MainViewOthello():
    def __init__(self, root, controller, game):
        self.controller = controller
        self.main_canvas = self.controller.tk.Canvas(
            root,
            width=controller.areas_size_config_dict["main_window"][0],
            height=controller.areas_size_config_dict["main_window"][1]
        )
        self.main_canvas.pack()
        self.grid_view = GridView(self.main_canvas, controller)
