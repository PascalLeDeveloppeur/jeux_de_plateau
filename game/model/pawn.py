from constants import FIRST_PAWN_TO_PLAY

class Pawn:
    """Create a pawn"""

    def __init__(self,
                 x_pos,
                 y_pos,
                 value1=None,
                 value2=None,
                 owner=None,
                 type_dict=None,
                 name=None
                 ):
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__value1 = value1
        self.__value2 = value2
        self.__owner = owner
        self.__type_dict = None
        self.__name = f"pawn_{x_pos}x{y_pos}" if name is None else name

    def get_x_pos(self):
        return self.__x_pos

    def get_y_pos(self):
        return self.__y_pos

    def get_value1(self):
        return self.__value1

    def get_value2(self):
        return self.__value2

    def get_owner(self):
        return self.__owner

    def get_type_dict(self):
        return self.__type_dict

    def get_name(self):
        return self.__name
