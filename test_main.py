import sys
from pprint import pprint
import numpy as np

from test_attack import *
from test_defend import *
from test_player import *
from test_Map import *
from bateau import *
from sous_marin import *


def main():
    player1 = test_player(5, 10, 5, 8, 4)
    test = test_attack()
    defend = test_defend()
    a = test.tire(0, 0, 1,player1, 1)
    b = defend.case_tire_1(7, 7, 1, player1, 1)
    pprint(player1.map.map_allied)
    c = defend.case_tire_1(10, 8, 1, player1, 1)
    pprint(test.map_enemy)
    print(a, b, c)


if __name__ == "__main__":
    main()
