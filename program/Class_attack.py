import numpy as np


class attack:
    def __init__(self):
        self.map_enemy = np.zeros(225 * 3)
        self.map_enemy.resize((3, 15, 15))
        self.tir = 0

    def tire(self, x, y, layer):
        # fonction envoie et attente de reponse
        touch = 1
        if touch == 1:
            self.map_enemy[layer, y, x] = 9
            return 1
        else:
            return 0

    def tire_x_case(self, x, y, layer, touch, number_case):
        if touch == 1:
            for i in range(number_case):
                for j in range(number_case):
                    self.map_enemy[layer, y + j, x + i] = 9
                return 1
        else:
            return 1
