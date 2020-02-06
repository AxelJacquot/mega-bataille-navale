from main import *
from player import *
from Map import *
from bateau import *
from sous_marin import *


class Player:
    def __init__(self, x_begin, x_finish, y_begin, y_finish, num_boat):
        self.name = ""
        self.map = Map()
        self.Surface = Boat()
        self.Profounder = SM()
        self.shoot = attack()
        self.place_boat = self.map.PSM(x_begin, x_finish, y_begin, y_finish, 2, num_boat)
        self.shooting = self.shoot.tire(7, 5, 2)
        self.shield = self.shoot.defend(9, 1, 0)
