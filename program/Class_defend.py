from program.Class_player import player


class defend:
    def case_tire_1(self, x, y, layer, player):
        if player.map_allied[layer, y, x] != 0:
            player.map_allied[layer, y, x] = 9
            self.touch = 1
        else:
            self.touch = 0
        return self.touch
