import numpy as np

from PySide2.QtCore import QObject, Slot

class attack(QObject):
    touch = 0

    def __init__(self):
        self.map_enemy = np.zeros(225 * 3)
        self.map_enemy.resize((3, 15, 15))   
        self.tir = 0

    def test_tire(x,y,layer):
        return 1

    @Slot(int, int, int)
    def tire(self, x, y, layer):
        # fonction envoie et attente de reponse
        if self.map_enemy[layer, y, x] != 9:
            self.map_enemy[layer, y, x] = 9
            touch = self.test_tire(x,y,layer)
            return touch

    def tire_x_case(self, x, y, layer, touch, number_case):
        if touch == 1:
            for i in range(number_case):
                for j in range(number_case):
                    self.map_enemy[layer, y + j, x + i] = 9
                    self.tir = 1
        else:
            self.tir = 0
            return self.tir
