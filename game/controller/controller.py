import sys

import tkinter as tk
from icecream import ic

from model.othello_game import OthelloGame
from model.player import Player
from view.grid_view import GridView
from view.main_view_othello import MainViewOthello


from module.debug_print import debug_print
from constants import (
    OTHELLO_TILE_HEIGHT,
    OTHELLO_TILE_WIDTH,
    PLAYER_NBR1,
    PLAYER_NBR2,
    YES,
)

from _config.size_config import areas_size_config_dict
from _config.objects_dict import objects_dict


class Controller:

    def __init__(self, player1_name, player2_name):
        self.areas_size_config_dict = areas_size_config_dict
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.tk = tk
        self.root = tk.Tk()
        self.nbr_of_cols = 0
        self.nbr_of_rows = 0
        self.game = None

    def run_othello(self):
        self.root.title("Othello")
        self.nbr_of_cols = 8
        self.nbr_of_rows = 8
        self.areas_size_config_dict["tile"] = {"width": OTHELLO_TILE_WIDTH,
                                     "height": OTHELLO_TILE_HEIGHT}

        self.areas_size_config_dict["pawn"] = {"width": OTHELLO_TILE_WIDTH,
                                     "height": OTHELLO_TILE_HEIGHT}

        self.areas_size_config_dict["grid"] = (
            self.nbr_of_cols * OTHELLO_TILE_WIDTH,
            self.nbr_of_rows * OTHELLO_TILE_HEIGHT)

        self.areas_size_config_dict["main_window"] = self.areas_size_config_dict["grid"]

        self.game = OthelloGame(self.player1.get_name(), self.player2.get_name())

        self.game.create_grid(self.nbr_of_cols,
                                self.nbr_of_rows)
        self.game.grid.create_tiles()
        self.game.grid.place_first_4_tiles(self)

        self.game.grid.empty_clickable_tiles_list()
        self.game.find_clickable_tiles()
        # TODO: Ensuite, je dois relancer la recherche à chaque clique sur une tuile clicable.

        #
        # view
        #
        self.main_view = MainViewOthello(self.root,
                                  self,
                                  self.game
        )

        self.root.mainloop()

    #
    # Event handlers
    #
    def tile_clicked(self, event, tile_view):

        debug_print("///" * 230, text_color_str="yellow", bg_color_str="black")
        debug_print(ic())
        print()
        print(f"tile.name: {tile_view.get_tile().get_name()}")
        print(f"tile.value: {tile_view.get_tile().get_owner}")
        print(f"event: {event}")
        print(f"mouse position (x,y): ({event.x},{event.y})")
        print()

        clicked_tile = tile_view.get_tile()
        print("------------- BEFORE ------------------")
        for y in range(0,8):
            for x in range(0,8):
                print(self.game.grid.get_tiles_dict()[f"{x}x{y}"].get_owner(), end="|")
            print("----------------------------------------")

        for straight_tiles_list in self.game.grid.get_clickable_tiles_list():
            for tile in straight_tiles_list:
                debug_print(tile.get_name(), "black", "green")
            print("----------------------------------------")

        for straight_tiles_list in self.game.grid.get_clickable_tiles_list():
            if clicked_tile == straight_tiles_list[0]:

                self.game.reverse_tiles_of_list(straight_tiles_list)
                self.game.change_player_to_play()
                self.game.grid.empty_clickable_tiles_list()
                self.game.find_clickable_tiles()
                # response = self.game.can_i_move(clicked_tile)
                # if response == True:
                #     debug_print("Placing the pawn")
                #     self.game.play_the_move(clicked_tile)
                #     debug_print("Pawn placed")
            # else:
            #     print()
            #     debug_print("Impossible de jouer à cet endroit !", "blue", "white")

        # Display the new pawn
        self.main_view.grid_view.display_pawns_views(self)

        print("------------- AFTER ------------------")
        for y in range(0,8):
            for x in range(0,8):
                print(self.game.grid.get_tiles_dict()[f"{x}x{y}"].get_owner(), end="|")
            print("----------------------------------------")
        print(f"C'est à {self.game.get_playername_to_play()} de jouer")
        print()
        print()
        print("\033[0;37;40m")
