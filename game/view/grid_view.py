from view.tile_view import TileView
from view.pawn_view import PawnView


class GridView:
    """Display the grid"""

    def __init__(self, parent_window, controller):
        self.__parent_window = parent_window
        self.__grid_canvas = controller.tk.Canvas(
            self.__parent_window,
            width=controller.areas_size_config_dict["grid"][0],
            height=controller.areas_size_config_dict["grid"][1],
            bg='red'
        )
        self.__grid_canvas.pack()
        self.__tiles_dict = controller.game.grid.get_tiles_dict()
        self.__tiles_views_list = []
        self.__pawns_views_list = []
        self.create_tiles_views(controller)
        self.display_pawns_views(controller)

    def create_tiles_views(self, controller):
        for tile in self.__tiles_dict.values():
            self.__tiles_views_list.append(TileView(self.__grid_canvas,
                                                   controller,
                                                   tile))

    def display_pawns_views(self, controller):
        for pawn in controller.game.get_pawns_list():
            self.__pawns_views_list.append(PawnView(self.__grid_canvas,
                                                   controller,
                                                   pawn))
