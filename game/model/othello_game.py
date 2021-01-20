import sys

from icecream import ic

from model.othello_grid import OthelloGrid
from model.player import Player
from model.pawn import Pawn
from module.debug_print import debug_print
from constants import (
    ERROR,
    KEY_ERROR,
    THERE_IS_NO_TILE,
    NO,
    NOT_YET,
    PLAYER_NBR1,
    PLAYER_NBR2,
    SUCCESS,
    THERE_IS_NO_TILE,
    TO_THE_BOTTOM,
    TO_THE_BOTTOM_LEFT,
    TO_THE_BOTTOM_RIGHT,
    TO_THE_LEFT,
    TO_THE_RIGHT,
    TO_THE_TOP,
    TO_THE_TOP_LEFT,
    TO_THE_TOP_RIGHT,
    YES,
    YES__NO_MORE_USED_TILE,
    YES__SAME_COLOR_REACHED
)


class OthelloGame:
    """
    Create the element that contains all the objects of the game
    as well as the game engine."""

    def __init__(self, player_name1, player_name2):
        self.player1 = Player(player_name1)
        self.player2 = Player(player_name2)
        self.grid = None
        self.__messages_area = None
        self.__nbr_of_cols = 0
        self.__nbr_of_rows = 0
        self.__all_directions_tuple = (
            TO_THE_TOP_LEFT,
            TO_THE_TOP,
            TO_THE_TOP_RIGHT,
            TO_THE_RIGHT,
            TO_THE_BOTTOM_RIGHT,
            TO_THE_BOTTOM,
            TO_THE_BOTTOM_LEFT,
            TO_THE_LEFT,
        )
        self.__player_to_play = PLAYER_NBR1
        self.__playername_to_play = player_name1
        self.__opponent_tile_value1 = 0
        self.__opponent_tile_value2 = 0
        self.__opponent_player = PLAYER_NBR2
        self.__pawns_list = []
        self.__checked_tile_position = {"x_pos": -10, "y_pos": -10}

    def get_pawns_list(self):
        return self.__pawns_list

    def get_opponent_player(self):
        return self.__opponent_player

    def get_player_to_play(self):
        return self.__player_to_play

    def get_playername_to_play(self):
        return self.__playername_to_play

    def set_player_to_play(self, player_nbr):
        self.__player_to_play = player_nbr

    def set_opponent_player(self, player_nbr):
        self.__opponent_player = player_nbr

    def set_playername_to_play(self, player_name):
        self.__playername_to_play = player_name

    def find_clickable_tiles(self):
        for tile_name in self.grid.get_tiles_dict():
            self.can_i_move(self.grid.get_tiles_dict()[tile_name])
        print(f"There are (is) {len(self.grid.get_clickable_tiles_list())} possible move(s).")

    def create_grid(self, nbr_of_cols, nbr_of_rows):
        self.__nbr_of_cols = nbr_of_cols
        self.__nbr_of_rows = nbr_of_rows

        self.grid = OthelloGrid(self.__nbr_of_cols, self.__nbr_of_rows)

    def place_pawn(
        self,
        x_pos,
        y_pos,
        value1=None,
        value2=None,
        owner=None,
        type_nbr=None,
        name=None,
    ):

        self.__pawns_list.append(
            Pawn(x_pos, y_pos, value1, value2, owner, type_nbr, name)
        )

    def play_the_move(self, clicked_tile):
        clicked_tile.set_owner(self.get_player_to_play())

        self.place_pawn(
            clicked_tile.get_x_pos(),
            clicked_tile.get_y_pos(),
            owner=self.get_player_to_play(),
            name=None,
        )

        self.change_player_to_play()

    def change_player_to_play(self):
        self.set_player_to_play(PLAYER_NBR2) if self.get_player_to_play() == PLAYER_NBR1 else self.set_player_to_play(PLAYER_NBR1)
        self.set_opponent_player(PLAYER_NBR2)\
                                      if self.__player_to_play == PLAYER_NBR1\
                                      else self.set_opponent_player(PLAYER_NBR1)
        self.change_playername_to_play()

    def change_playername_to_play(self):
        self.set_playername_to_play(self.player1.get_name())\
            if self.get_player_to_play() == PLAYER_NBR1\
            else self.set_playername_to_play(self.player2.get_name())

    def can_i_move(self, clicked_tile):
        is_move_ok = False
        if clicked_tile.is_empty():
            reversible_tiles_from_this_location = [clicked_tile]
            for direction in self.__all_directions_tuple:
                # import ipdb; ipdb.set_trace()
                # debug_print(f"Can I move {direction}?", text_color_str="white", bg_color_str="black")
                response = self.check_direction(
                    clicked_tile,
                    direction,
                    reversible_tiles_from_this_location)
                if response == True:
                    is_move_ok == True
        return True if is_move_ok else False

    def check_direction(self,
                        clicked_tile,
                        direction,
                        reversible_tiles_from_this_location):
        """
        In the given direction, check if there is a tile of the same value as
        the current player's one.
        The status returns SUCCESS or THERE_IS_NO_TILE or the raised exception
        << Did I succeed in getting a tile ? >>"""

        reference_tile = clicked_tile
        next_tile, status = self.give_me_next_tile(reference_tile, direction)

        # ic()
        # if next_tile:
            # debug_print(f"next tile: {next_tile.get_name()} --- Status: {status}")
        # else:
        #     debug_print("No tile")
        if status == THERE_IS_NO_TILE:
            # print(THERE_IS_NO_TILE, direction)
            return False
        if self.is_error(status, direction):
            return False
        if not self.is_the_opponent_tile(next_tile):
            # print(f"The next pawn {direction} is not the one of the player nbr", self.get_opponent_player())
            return False
        # ic()
        # debug_print("Next tile: ", next_tile.get_name())
        # debug_print(f"La tuile suivante est à la position: {next_tile.get_name()}. Propriétaire de la tuile suivante: {next_tile.get_owner()} --- Le joueur adverse est le joueur nbr{self.get_opponent_player()}", "black", "green")

        has_browsed_the_max_of_tiles_in_this_direction = NOT_YET
        while has_browsed_the_max_of_tiles_in_this_direction == NOT_YET:

            # print(f"Direction: {direction} --- Est-ce une case adverse ?: {self.is_the_opponent_tile(next_tile)} --- Position: {next_tile.get_name()}")
            if self.is_the_opponent_tile(next_tile):
                reversible_tiles_from_this_location.append(next_tile)

            reference_tile = next_tile
            next_tile, status = self.give_me_next_tile(reference_tile, direction)

            if self.is_error(status, direction) or next_tile.is_empty():
                has_browsed_the_max_of_tiles_in_this_direction =\
                    YES__NO_MORE_USED_TILE
            if self.is_the_tile_of_the_current_player(next_tile):
                has_browsed_the_max_of_tiles_in_this_direction =\
                    YES__SAME_COLOR_REACHED

        if has_browsed_the_max_of_tiles_in_this_direction ==\
                YES__NO_MORE_USED_TILE:
            # print(YES__NO_MORE_USED_TILE, " after this one.")
            reversible_tiles_from_this_location = None
            return False
        if has_browsed_the_max_of_tiles_in_this_direction ==\
                YES__SAME_COLOR_REACHED:
            # print(YES__SAME_COLOR_REACHED)
            self.grid.add_to_clickable_tiles_list(
                reversible_tiles_from_this_location)
            # print(f"reversible tiles: {len(reversible_tiles_from_this_location)}")
            return True

    def give_me_next_tile(self, reference_tile, direction):
        """
        Return the next tile according to the given direction
        and the status (did I succeed in finding a tile)"""
        x_dir = y_dir = 0
        if direction == TO_THE_TOP_LEFT:
            x_dir = -1
            y_dir = -1
        if direction == TO_THE_TOP:
            y_dir = -1
        if direction == TO_THE_TOP_RIGHT:
            x_dir = 1
            y_dir = -1
        if direction == TO_THE_RIGHT:
            x_dir = 1
        if direction == TO_THE_BOTTOM_RIGHT:
            x_dir = 1
            y_dir = 1
        if direction == TO_THE_BOTTOM:
            y_dir = 1
        if direction == TO_THE_BOTTOM_LEFT:
            x_dir = -1
            y_dir = 1
        if direction == TO_THE_LEFT:
            x_dir = -1

        try:
            return (
                self.grid.get_tiles_dict()[
                    f"{reference_tile.get_x_pos() + x_dir}"
                    + f"x{reference_tile.get_y_pos() + y_dir}"
                ],
                SUCCESS,
            )
        except KeyError:  # That means there is no more tile
            return (None, THERE_IS_NO_TILE)
        except Exception as e:
            debug_print("", text_color_str="white", bg_color_str="black")
            return (None, ERROR + " " + str(e))

    def is_error(self, status, direction):
        # print("Status: ", status)
        if status == THERE_IS_NO_TILE:
            print(THERE_IS_NO_TILE, direction)
            return True
        elif status.startswith(ERROR):
            # print(f"ERROR while looking for a tile {direction}")
            # print("The reason is: ", status)
            return True
        return False

    def is_the_opponent_tile(self, next_tile=None):
        if next_tile:
            return next_tile.get_owner() == self.get_opponent_player()
        return False

    def is_player_nbr1_playing(self):
        return self.__player_to_play == PLAYER_NBR1

    def is_the_tile_of_the_current_player(self, next_tile):
        if next_tile:
            return next_tile.get_owner() == self.get_player_to_play()

    def reverse_tiles_of_list(self, list_of_tiles):
        for tile_to_reverse in list_of_tiles:
            tile_to_reverse.set_owner(self.get_player_to_play())
            self.place_pawn(tile_to_reverse.get_x_pos(),
                            tile_to_reverse.get_y_pos(),
                            owner=tile_to_reverse.get_owner())

