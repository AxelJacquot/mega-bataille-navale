from program.Class_player import player, map_allied


class defend:
    def __init__(self):
        self.touch = 0

    def case_tire_1(self, x, y, layer, tir):

        if tir == 1:
            if map_allied[layer, y, x] != 0:
                map_allied[layer, y, x] = 9
                self.touch = 1
            else:
                self.touch = 0
            return self.touch
        if tir == 2:
            if map_allied[layer, y, x] != 0:
                for i in range(2):
                    for j in range(2):
                        if map_allied[layer, y + j, x + i] != 0:
                            map_allied[layer, y + j, x + i] = 9
                        else:
                            pass
            return self.touch
