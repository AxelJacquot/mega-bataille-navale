from Class_attack import attack
from Class_defend import defend
from Class_Map import Map
from bateau import Boat
from sous_marin import SM


class player:
    def __init__(self, x_begin, x_finish, y_begin, y_finish, num_boat):
        self.name = ""
        self.map = Map()
        self.Surface = Boat()
        self.Profounder = SM()
        self.place_boat = self.map.PSM(x_begin, x_finish, y_begin, y_finish, 1, num_boat)

