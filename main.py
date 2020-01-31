import sys


class Player:
    def __init__(self, x_begin, x_finish, y_begin, y_finish):
        self.name = ""
        self.Map = Map()
        self.Surface = Boat()
        self.Profounder = SM()
        self.Map.PBoat(x_begin, x_finish, y_begin, y_finish)


class Map:
    def __init__(self, size_x=15, size_y=15, layer=3):
        self.map_allied = [["0"] * size_x] * size_y
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.Player = Player

    def PBoat(self, x_begin, x_finish, y_begin, y_finish):
        for x in range(15):
            for y in range(15):
                if x_begin <= x:
                    if x <= x_finish:
                        if y_begin <= y:
                            if y <= y_finish:
                                if self.map_allied[x][y] == "0":
                                    self.map_allied[x][y].replace("0", "4")
        print(self.map_allied)


class Boat:
    def __init__(self, size_x=0, size_y=0, layer=1):
        self.size_x = size_x
        self.size_y = size_y

        self.layer = layer
        self.container = Container()

        self.PA_1 = PA()
        self.PA_2 = PA()

        self.destroyer_1 = Destroyer()
        self.destroyer_2 = Destroyer()
        self.destroyer_3 = Destroyer()

        self.Tor_1 = Tor()
        self.Tor_2 = Tor()
        self.Tor_3 = Tor()


class Container:
    def __init__(self, size_x=5, size_y=2, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class Destroyer:
    def __init__(self, size_x=4, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class PA:
    def __init__(self, size_x=5, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class Tor:
    def __init__(self, size_x=4, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class SM:
    def __init__(self):
        self.PSM_1 = PSM()
        self.PSM_2 = PSM()
        self.PSM_3 = PSM()
        self.PSM_4 = PSM()
        self.PSM_5 = PSM()

        self.MSM_1 = MSM()
        self.MSM_2 = MSM()

        self.SMNuclear_1 = SMNuclear()
        self.SMNuclear_2 = SMNuclear()


class SMNuclear:
    def __init__(self, size_x=0, size_y=0, layer=2):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class PSM:
    def __init__(self, size_x=3, size_y=1, layer=2):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class MSM:
    def __init__(self, size_x=2, size_y=1, layer=2):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class attack:
    pass


def main():
    player1 = Player(5, 10, 4, 6)


if __name__ == "__main__":
    main()
