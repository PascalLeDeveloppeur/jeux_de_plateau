class Player:
    """Create a player who has a name, points, pawns, and so on."""

    def __init__(self, name):
        self.__name = name
        self.__points = 0
        self.__pawns_qty = 1000
        self.__number_of_moves = 0

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def get_pawns_qty(self):
        return self.__pawns_qty

    def get_number_of_moves(self):
        return self.__number_of_moves
