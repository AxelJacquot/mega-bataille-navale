from attack import *
from defend import *
from player import *
from Map import *
from bateau import *
from sous_marin import *


class player:
    def __init__(self, x_begin, x_finish, y_begin, y_finish, num_boat):
        self.name = ""
        self.map = Map()
        self.Surface = Boat()
        self.Profounder = SM()
        self.place_boat = self.map.PSM(x_begin, x_finish, y_begin, y_finish, 1, num_boat)

