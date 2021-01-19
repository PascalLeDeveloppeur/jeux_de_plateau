import sys

from controller.controller import Controller


args_list = sys.argv
if not len(args_list) == 5:
    print()
    print("Erreur !")
    print("Pour démarrer un jeu, il faut érire comme ce qui suit :")
    print("python3 game othello Pascal vs Lisa")
    print()
    print("Si ça ne fonctionne pas, essayez ce qui suit:")
    print("python game othello Pascal vs Lisa")
    print()
    sys.exit()

game_name = args_list[1]
player1_name = args_list[2]
player2_name = args_list[4]

controller = Controller(player1_name, player2_name)

games_dict = {
    "othello": controller.run_othello,
}

games_dict[f"{game_name}"]()
