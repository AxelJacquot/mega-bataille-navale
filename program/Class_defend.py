from program.Class_player import player, map_allied
from PySide2.QtCore import QObject, Signal, Property

class defend(QObject):

    def __init__(self):
        super(defend,self).__init__()
        self.touch = 0

    def case_tire_1(self, x, y, layer, tir):

        if tir == 1:
            if map_allied[layer, y, x] != 0:
                map_allied[layer, y, x] = 9
                self.touch = 1
            else:
                self.touch = 0
            return self.touch

