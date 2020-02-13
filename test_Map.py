from test_attack import *
from test_defend import *
from test_player import *
from test_Map import *
from bateau import *
from sous_marin import *
import numpy as np


class test_Map:
    def __init__(self, size_x=15, size_y=15, layer=2):
        self.error = -1
        self.map_allied = np.zeros(225 * 3)
        self.map_allied.resize((3, 15, 15))
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer

    def PSM(self, x_begin, x_finish, y_begin, y_finish, layer, num_sm):
        if 0 > x_begin < 15:
            return "x_begin case hors-map"
        elif 0 > x_finish < 15:
            return "x_ finish case hors-map"
        elif 0 > y_begin < 15:
            return "y_begin case hors-map"
        elif 0 > y_finish < 15:
            return "y_ finish case hors-map"
        elif 0 > layer < 3:
            return "couche hors de portée"
        elif y_begin >= y_finish:
            return "error la valeur y_begin ne peut pas être supérieur à celle de fin"
        elif x_begin >= x_finish:
            return "error la valeur x_begin ne peut pas être supérieur à celle de fin"
        else:
            for y in range(15):
                for x in range(15):
                    if y_begin <= y <= y_finish and x_begin <= x <= x_finish:
                        if self.map_allied[layer, y, x] != 0:
                            return "error : Case Prise"
                        else:
                            if num_sm == 1:
                                self.map_allied[layer, y, x] = 1
                            if num_sm == 2:
                                self.map_allied[layer, y, x] = 2
                            if num_sm == 3:
                                self.map_allied[layer, y, x] = 3
                            if num_sm == 4:
                                self.map_allied[layer, y, x] = 4
                            if num_sm == 5:
                                self.map_allied[layer, y, x] = 5
                            if num_sm == 6:
                                self.map_allied[layer, y, x] = 6
                            if num_sm == 7:
                                self.map_allied[layer, y, x] = 7
# num_sm
# 1 => porte-container
# 2 => porte-avion
# 3 => destroyer
# 4 => torpilleur
# 5 => sous-marin
# 6 => petit-sous-marin
# 7 => mini-sous-marin
