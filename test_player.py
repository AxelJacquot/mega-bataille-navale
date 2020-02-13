from test_attack import *
from test_defend import *
from test_player import *
from test_Map import *
from bateau import *
from sous_marin import *


class test_player:
    def __init__(self, x_begin, x_finish, y_begin, y_finish, num_boat):
        self.name = ""
        self.map = test_Map()
        self.Surface = Boat()
        self.Profounder = SM()
        self.place_boat = self.map.PSM(x_begin, x_finish, y_begin, y_finish, 1, num_boat)

