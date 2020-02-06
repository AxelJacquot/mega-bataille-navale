import sys
from pprint import pprint
import numpy as np

from player import *
from Map import *
from bateau import *
from sous_marin import *

class attack:
    def __init__(self, touch=0):
        self.touch = touch
        self.map_ennemy = [[[0] * 15] * 15] * 3

    def tire(self, x, y, layer):
        pprint(self.map_ennemy)
        if (self.map_ennemy[x][y][layer] != 0):
            self.map_ennemy[x][y][layer] = "X"
            return "Tire a atteint sa cible"
        else:
            return "Tire dans le vide"


class defend:
    def __init__(self, touch=0):
        self.touch = touch

    def case_touche(self, x, y, layer):
        if Player.map.map_allied[x][y][layer] != 0:
            Player.map.map_allied[x][y][layer] = "X"
            touch = 1
        else:
            touch = 0
        return touch


def main():
    player1 = Player(0, 10, 8, 0, 2)
    print(player1.place_boat)
    player1.shoot.map_ennemy[7][5][0] = 1
    pprint(player1.map.map_allied)


if __name__ == "__main__":
    main()
