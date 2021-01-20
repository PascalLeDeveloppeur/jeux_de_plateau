from module.debug_print import debug_print

from constants import ( COLORS_DICT,
                        PLAYER_NBR1,)


class PawnView:
    """Display a pawn"""

    def __init__(self, grid_canvas, controller, pawn):
        self.__width =\
            controller.areas_size_config_dict["pawn"]["width"]

        self.__height =\
            controller.areas_size_config_dict["pawn"]["height"]

        self.__pawn = pawn
        self.__color_nbr = 1
        self.__border_color_nbr = 0
        self.display_pawn(grid_canvas, controller)

    def get_color_nbr(self):
        return self.__color_nbr

    def get_border_color_nbr(self):
        return self.__border_color_nbr

    def set_color_nbr(self, color_nbr):
        self.__color_nbr = color_nbr

    def set_border_color_nbr(self, border_color_nbr):
        self.__border_color_nbr = border_color_nbr

    def display_pawn(self, grid_canvas, controller):

        self.top_left_x_pos =\
            self.__pawn.get_x_pos() * self.__width

        self.top_left_y_pos =\
            self.__pawn.get_y_pos() * self.__height

        self.bottom_right_x_pos =\
            self.top_left_x_pos + self.__width

        self.bottom_right_y_pos =\
            self.top_left_y_pos + self.__height

        self.__border_color_nbr = 0 if self.__pawn.get_owner() == PLAYER_NBR1 else 1

        grid_canvas.create_oval(
            self.top_left_x_pos,
            self.top_left_y_pos,
            self.bottom_right_x_pos,
            self.bottom_right_y_pos,
            fill=COLORS_DICT[self.__pawn.get_owner()],
            outline=COLORS_DICT[self.__border_color_nbr]
        )

        # To ensure that the pawn view has the focus on it
        grid_canvas.focus_set()
