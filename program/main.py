from pprint import pprint
from program.Class_attack import attack
from program.Class_player import player
from program.Class_defend import defend


def main():
    x = 0
    y = 0
    layer = 0
    player1 = player()
    test = player1.PSM(4, 2, 2, 5, 0, 1)
    test3 = player1.PSM(6, 5, 2, 7, 0, 1)

    test1 = defend()
    test2 = test1.case_tire_1(4, 2, 2, 1)
    pprint(player1.map_allied)
    print(test2)


if __name__ == "__main__":
    main()
