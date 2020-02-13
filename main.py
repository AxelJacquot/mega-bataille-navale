import sys
from pprint import pprint
import numpy as np

from player import *
from Map import *
from bateau import *
from sous_marin import *


class attack:

    def __init__(self):
        self.touch = 0
        self.map_enemy = np.zeros(225 * 3)
        self.map_enemy.resize((3, 15, 15))

    def tire(self, x, y, layer, touche=0):
        if touche == 0:
            self.map_enemy[layer, y, x] = 1
            result = 0
            return result
        if touche == 1:
            self.map_enemy[layer, y, x] = 9
            result = 1
            return result


class defend:
    def __init__(self):
        self.tire = 0
        self.touch = 0

    def case_tire_1(self, x, y, layer, player):
        if self.tire == 1:
            if player.map.map_allied[layer, y, x] != 0:
                player.map.map_allied[layer, y, x] = 9
                self.touch = 1
            else:
                self.touch = 0
            return

    def case_tire_2(self, x, y, layer, player):
        if self.tire == 2:
            if player.map.map_allied[layer, y, x] != 0:
                for i in range(2):
                    pass


def main():
    player1 = Player(5, 10, 5, 8, 4)
    test = attack()
    test_defend = defend()
    a = test.tire(7, 7, 1)
    test_defend.case_tire_1(9, 8, 1, player1, 1)
    print(a)
    print(b)
    pprint(player1.map.map_allied)


if __name__ == "__main__":
    main()
