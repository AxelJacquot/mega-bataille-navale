from program.sous_marin import SM, SMNuclear, PSM, MSM
from program.bateau import Boat, Container, Destroyer, PA, Tor
import numpy as np


class Map:
    def __init__(self, size_x=15, size_y=15, layer=2):
        self.error = -1
        self.map_allied = np.zeros(225 * 3)
        self.map_allied.resize((3, 15, 15))
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def test(self, x, y, layer, type_boat, index, orientation,player):
        if type_boat == 1:
            self.error = player.container.place_boat(x,y,type_boat, index, orientation)
        if type_boat == 2:
            self.error = player.destroyer.place_boat(x,y,type_boat, index, orientation)
        if type_boat == 3:
            self.error = player.pa.place_boat(x,y,type_boat, index, orientation)
        if type_boat == 4:
            self.error = player.tor.place_boat(x,y,type_boat, index, orientation)
        if type_boat == 5:
            self.error = player.SMNuclear_1.place_boat(x,y,type_boat, index, orientation)
        if type_boat == 6:
            self.error = player.PSM_1.place_boat(x,y,type_boat, index, orientation)
        if type_boat == 7:
            self.error = player.MSM_1.place_boat(x,y,type_boat, index, orientation)



    def PSM(self, x_begin, y_begin, layer, num_sm, index, orientation, player):
        self.error = 0 
        self.error = self.test(x_begin,y_begin, layer, num_sm, index, orientation, player)

        if self.error == 0:
            if 0 >= x_begin < 15:
                self.error = 1
                return self.error
            elif 0 >= self.x_finish < 15:
                self.error = 1
                return self.error
            elif 0 >= self.y_finish < 15:
                self.error = 1
                return self.error
            elif 0 >= self.x_finish < 15:
                self.error = 1
                return self.error
            elif 0 > layer <= 3:
                self.error = 1
                return self.error
            elif y_begin >= self.y_finish:
                self.error = 1
                return self.error
            elif x_begin >= self.x_finish:
                self.error = 1
                return self.error
            else:
                for y in range(15):
                    for x in range(15):
                        if y_begin <= y <= self.y_finish and x_begin <= x <= self.x_finish:
                            if self.map_allied[layer, y, x] != 0:
                                self.error = 1
                                return self.error
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
