from constants import ( BORDER_COLOR_NBR,
                        COLOR_NBR,
                        COLORS_DICT,
                        OTHELLO_TILE_DICT,)


class TileView:
    """Display a tile"""

    def __init__(self, grid_canvas, controller, tile):
        self.__tile_width = controller.areas_size_config_dict["tile"]["width"]
        self.__tile_height = controller.areas_size_config_dict["tile"]["height"]
        self.__tile = tile
        self.__top_left_x_pos = 0
        self.__top_left_y_pos = 0
        self.__bottom_right_x_pos = 0
        self.__bottom_right_y_pos = 0
        self.display_tile(grid_canvas, controller)

    def get_tile(self):
        return self.__tile

    def display_tile(self, grid_canvas, controller):
        self.__top_left_x_pos = self.__tile.get_x_pos() * self.__tile_width
        self.__top_left_y_pos = self.__tile.get_y_pos() * self.__tile_height
        self.__bottom_right_x_pos = (self.__top_left_x_pos + self.__tile_width)
        self.__bottom_right_y_pos = (self.__top_left_y_pos + self.__tile_height)

        grid_canvas.create_rectangle(
            self.__top_left_x_pos,
            self.__top_left_y_pos,
            self.__bottom_right_x_pos,
            self.__bottom_right_y_pos,
            fill=COLORS_DICT[self.__tile.get_type_dict()[COLOR_NBR]],
            outline=COLORS_DICT[self.__tile.get_type_dict()[BORDER_COLOR_NBR]],
            tags=self.__tile.get_name(),
        )

        grid_canvas.tag_bind(
            self.__tile.get_name(),
            "<Button-1>",
            lambda event: controller.tile_clicked(event, self)
        )

        grid_canvas.focus_set() # To ensure that the tile has the focus on it
