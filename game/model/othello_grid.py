from model.tile import Tile
from constants import ( OTHELLO_TILE_DICT,
                        PLAYER_NBR1,
                        PLAYER_NBR2,)


class OthelloGrid:
    """Create the grid which itself will create the tiles """

    def __init__(self, nbr_of_cols, nbr_of_rows):
        self.__nbr_of_cols = nbr_of_cols
        self.__nbr_of_rows = nbr_of_rows
        self.__tiles_dict = {}
        self.__clickable_tiles_list = []

    def get_tiles_dict(self):
        return self.__tiles_dict

    def get_clickable_tiles_list(self):
        return self.__clickable_tiles_list

    def add_to_clickable_tiles_list(self, tiles_list):
        self.__clickable_tiles_list.append(tiles_list)

    def empty_clickable_tiles_list(self):
        self.__clickable_tiles_list = []

    def create_tiles(self):
        """Create the tiles of the grid"""

        for y_pos in range(self.__nbr_of_cols):
            for x_pos in range(self.__nbr_of_rows):
                self.get_tiles_dict()[f"{str(x_pos)}x{str(y_pos)}"] =\
                    Tile(x_pos,
                         y_pos,
                         owner=0,
                         tile_type_dict=OTHELLO_TILE_DICT)

    def place_first_4_tiles(self, controller):
        self.place_tile_of_player(PLAYER_NBR1, tile=self.get_tiles_dict()["3x3"])
        self.place_tile_of_player(PLAYER_NBR1, tile=self.get_tiles_dict()["4x4"])
        self.place_tile_of_player(PLAYER_NBR2, tile=self.get_tiles_dict()["4x3"])
        self.place_tile_of_player(PLAYER_NBR2, tile=self.get_tiles_dict()["3x4"])
        self.place_tile_of_player(PLAYER_NBR2, tile=self.get_tiles_dict()["3x5"])
        self.place_tile_of_player(PLAYER_NBR2, tile=self.get_tiles_dict()["3x6"])

        for one_tile in (self.get_tiles_dict()["3x3"],
                         self.get_tiles_dict()["4x4"],
                         self.get_tiles_dict()["4x3"],
                         self.get_tiles_dict()["3x4"],
                         self.get_tiles_dict()["3x5"],
                         self.get_tiles_dict()["3x6"]):

            controller.game.place_pawn(
                                        one_tile.get_x_pos(),
                                        one_tile.get_y_pos(),
                                        owner=one_tile.get_owner(),)

    def place_tile_of_player(self, player_nbr, tile):
        tile.set_owner(player_nbr)



