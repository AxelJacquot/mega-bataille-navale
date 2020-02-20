import numpy as np

from PySide2.QtCore import QObject, Slot


class attack(QObject):
    def __init__(self):
        super(attack, self).__init__()
        self.map_enemy = np.zeros(225 * 3)
        self.map_enemy.resize((3, 15, 15))
        self.tir = 0
        self.touch = 0

    def test_tire(self,x, y, layer):
        return 1

    @Slot(int, int, int)
    def tire(self, x, y, layer):
        # fonction envoie et attente de reponse
        if self.map_enemy[layer, y, x] != 0:
            self.map_enemy[layer, y, x] = 9
            self.touch = self.test_tire(x, y, layer)
            return self.touch


