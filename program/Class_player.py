from program.sous_marin import SM, SMNuclear, PSM, MSM
from program.bateau import Boat, Container, Destroyer, PA, Tor
import numpy as np


class player:
    def __init__(self, size_x=15, size_y=15, layer=2):
        self.name = ""
        self.error = 0
        self.map_allied = np.zeros(225 * 3)
        self.map_allied.resize((3, 15, 15))
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0
        self.container = Container()
        self.pa = PA()
        self.destroyer = Destroyer()
        self.tor = Tor()
        self.PSM_1 = PSM()
        self.MSM_1 = MSM()
        self.SMNuclear_1 = SMNuclear()

    def PSM(self, x_begin, y_begin, layer, type_boat, index, orientation):
        if type_boat == 1:
            self.error = self.container.place_boat(x_begin, y_begin, type_boat, index, orientation)
            self.y_finish = self.container.y_finish
            self.x_finish = self.container.x_finish
        elif type_boat == 2:
            self.error = self.destroyer.place_boat(x_begin, y_begin, type_boat, index, orientation)
            self.y_finish = self.destroyer.y_finish
            self.x_finish = self.destroyer.x_finish
        elif type_boat == 3:
            self.error = self.pa.place_boat(x_begin, y_begin, type_boat, index, orientation)
            self.y_finish = self.pa.y_finish
            self.x_finish = self.pa.x_finish
        elif type_boat == 4:
            self.error = self.tor.place_boat(x_begin, y_begin, type_boat, index, orientation)
            self.y_finish = self.tor.y_finish
            self.x_finish = self.tor.x_finish
        elif type_boat == 5:
            self.error = self.SMNuclear_1.place_boat(x_begin, y_begin, type_boat, index, orientation)
            self.y_finish = self.SMNuclear_1.y_finish
            self.x_finish = self.SMNuclear_1.x_finish
        elif type_boat == 6:
            self.error = self.PSM_1.place_boat(x_begin, y_begin, type_boat, index, orientation)
            self.y_finish = self.PSM_1.y_finish
            self.x_finish = self.PSM_1.x_finish
        elif type_boat == 7:
            self.error = self.MSM_1.place_boat(x_begin, y_begin, type_boat, index, orientation)
            self.y_finish = self.MSM_1.y_finish
            self.x_finish = self.MSM_1.x_finish

        if self.error is None:
            if 0 > x_begin > 15:
                self.error = 1
                return self.error
            elif 0 > self.x_finish > 15:
                self.error = 1
                return self.error
            elif 0 > self.y_finish > 15:
                self.error = 1
                return self.error
            elif 0 > self.x_finish > 15:
                self.error = 1
                return self.error
            elif 0 > layer > 3:
                self.error = 1
                return self.error
            elif y_begin > self.y_finish:
                self.error = 1
                return self.error
            elif x_begin > self.x_finish:
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
                                 self.map_allied[layer, y, x] = type_boat
        if self.error == 1:
            return 1
# num_sm
# 1 => porte-container
# 2 => porte-avion
# 3 => destroyer
# 4 => torpilleur
# 5 => sous-marin
# 6 => petit-sous-marin
# 7 => mini-sous-marin
