from program.LogicGame.sous_marin import SMNuclear, PSM, MSM
from program.LogicGame.bateau import Container, Destroyer, PA, Tor
import numpy as np
from PySide2.QtCore import QObject, Slot

map_allied = np.zeros(225 * 3)
map_allied.resize((3, 15, 15))

boat = np.zeros(200)
boat.resize(8, 5, 5)


class player(QObject):
    def __init__(self, size_x=15, size_y=15, layer=2):
        super(player,self).__init__()
        self.name = ""
        self.error = 0
        self.map_allied = map_allied
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

    @Slot(int,int,int,int,int,bool, result=bool)
    def PSM(self, x_begin, y_begin, layer, type_boat, index, orientation):
        print(x_begin, y_begin, layer, type_boat, index, orientation)
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
            if 0 > layer > 3:
                self.error = 1
                return False
            elif y_begin > self.y_finish:
                self.error = 1
                return False
            elif x_begin > self.x_finish:
                self.error = 1
                return False
            else:
                for y in range(15):
                    for x in range(15):
                        if y_begin <= y <= self.y_finish and x_begin <= x <= self.x_finish:
                            if self.map_allied[layer, y, x] != 0:
                                self.error = 1
                                return False
                            else:
                                self.map_allied[layer, y, x] = type_boat
        if self.error == 1:
            return False
        else:
            boat[type_boat][index] = [x_begin, self.x_finish, y_begin, self.y_finish, layer]
            return True
# num_sm
# 1 => porte-container
# 2 => porte-avion
# 3 => destroyer
# 4 => torpilleur
# 5 => sous-marin
# 6 => petit-sous-marin
# 7 => mini-sous-marin
