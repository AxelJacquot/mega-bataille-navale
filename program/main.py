from pprint import pprint
from program.Class_attack import attack
from program.Class_player import player
from program.Class_defend import defend


def main():
    x = 0
    y = 0
    layer = 0
    player1 = player()
    test1 = player1.map.PSM(x,y,layer, 4, 2, 0, player1)
    pprint(player1.map.map_allied)
    print(test1)


if __name__ == "__main__":
    main()

