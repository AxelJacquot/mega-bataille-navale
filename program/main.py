import sys
from pprint import pprint
import numpy as np


from program.attack import attack
from program.defend import defend
from program.player import player


def main():
    player1 = player(5, 10, 5, 8, 4)
    test = attack()
    t_defend = defend()
    a = test.tire(0, 0, 1,player1, 0)
    b = t_defend.case_tire_1(7, 7, 1, player1, 0)
    pprint(player1.map.map_allied)
    c = t_defend.case_tire_1(10, 8, 1, player1, 1)
    pprint(test.map_enemy)
    print(a, b, c)


if __name__ == "__main__":
    main()

