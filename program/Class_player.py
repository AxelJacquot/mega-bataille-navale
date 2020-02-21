from program.sous_marin import SMNuclear, PSM, MSM
from program.bateau import Container, Destroyer, PA, Tor
import numpy as np

map_allied = np.zeros(225 * 3)
map_allied.resize((3, 15, 15))


class player:
    def __init__(self, size_x=15, size_y=15, layer=2):
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

# need a slot
    def cleanBoat(self, y_begin, y_finish, x_begin, x_finish, layer, type_boat):
        for y in range(y_begin, y_finish + 1):
            for x in range(x_begin, x_finish + 1):
                if y_begin <= y <= y_finish and x_begin <= x <= x_finish:
                    if self.map_allied[layer, y, x] == type_boat:
                        self.map_allied[layer, y, x] = 0

    def PSM(self, x_begin, y_begin, layer, type_boat, index, orientation):
<<<<<<< HEAD
        """
            Fuck x_begin : first position of the boat on x axe.
                 y_begin : first position of the boat on y axe.
                 Type boat
                    1 => porte-container
                    2 => porte-avion
                    3 => destroyer
                    4 => torpilleur
                    5 => sous-marin
                    6 => petit-sous-marin
                    7 => mini-sous-marin
                index : number of the ship
                Orientation => 1 => Horizontale
                Orientation => 0 => Verticale
            PS :x_max = 15 y_max = 15
        """
=======
        if 0 > layer > 3:
            self.error = 1
            return self.error
>>>>>>> db4476d15f87a93d028b18c354af154b889c9c77
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
            if y_begin > self.y_finish:
                self.error = 1
                return self.error
            elif x_begin > self.x_finish:
                self.error = 1
                return self.error
            else:
                for y in range(y_begin, self.y_finish + 1):
                    for x in range(x_begin, self.x_finish + 1):
                        if y_begin <= y <= self.y_finish and x_begin <= x <= self.x_finish:
                            if self.map_allied[layer, y, x] != 0:
                                self.error = 1
                                return self.error
                            else:
                                self.map_allied[layer, y, x] = type_boat
        if self.error == 1:
            self.cleanBoat(y_begin, self.y_finish, x_begin, self.x_finish, layer, type_boat)
            return 1




# num_sm
# 1 => porte-container
# 2 => porte-avion
# 3 => destroyer
# 4 => torpilleur
# 5 => sous-marin
# 6 => petit-sous-marin
# 7 => mini-sous-marin
