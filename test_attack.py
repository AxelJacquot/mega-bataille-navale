from test_defend import *
from test_player import *
from test_Map import *
from bateau import *
from sous_marin import *


class test_attack:
    touch = 0

    def __init__(self):
        self.map_enemy = np.zeros(225 * 3)
        self.map_enemy.resize((3, 15, 15))
        self.tir = 0

    def tire(self, x, y, layer, player, touch):
        # fonction envoie et attente de reponse
        if touch == 1:
            self.map_enemy[layer, y, x] = 9
            self.tir = 1
            return self.tir
        else:
            self.tir = 0
            return self.tir

    def tire_2_case(self, x, y, layer, touch):
        if touch == 1:
            for i in range(2):
                for j in range(2):
                    if self.map_enemy[layer, y + j, x + i] != 0:
                        self.map_enemy[layer, y + j, x + i] = 9
                        self.tir = 1
                    else:
                        self.tir = 0
        else:
            self.tir = 0
            return self.tir
