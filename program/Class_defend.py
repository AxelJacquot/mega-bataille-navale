from program.Class_player import player


class defend:
    def case_tire_1(self, x, y, layer, tir, player):
        if tir == 1:
            if player.map_allied[layer, y, x] != 0:
                player.map_allied[layer, y, x] = 9
                self.touch = 1
            else:
                self.touch = 0
            return self.touch
        if tir == 2:
            if player.map_allied[layer, y, x] != 0:
                for i in range(2):
                    for j in range(2):
                        if player.map_allied[layer, y + j, x + i] != 0:
                            player.map_allied[layer, y + j, x + i] = 9
                            self.touch = 1
                        else:
                            self.touch = 0
            return self.touch
