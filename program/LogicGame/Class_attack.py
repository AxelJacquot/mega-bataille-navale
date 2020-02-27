import numpy as np

from PySide2.QtCore import QObject, Slot, Signal


class Attack(QObject):
    

    TargetShoot = Signal(int, int, int)
    Target = Signal()
    TargetQMl = Signal(int, int, int, bool)

    def __init__(self):
        super(Attack, self).__init__()
        self.map_enemy = np.zeros(225 * 3)
        self.map_enemy.resize((3, 15, 15))
        self.touch = False
        self.x = 0
        self.y = 0
        self.tir = 0

    @Slot(int, int)
    def tire(self, x, y):
        print("Tire")
        print(x, y)
        # fonction envoie et attente de reponse
        self.x = x
        self.y = y
        x += 1
        y += 1
        self.TargetShoot.emit(2 ,x, y)
        #self.Target.emit()

    @Slot(int, int)
    def tire2(self, resultShoot, coule):
<<<<<<< HEAD
        self.touch = False
=======
        print("Result Shoot: " , resultShoot, " Coule :", coule)
        touch = False
>>>>>>> a256c2acd1269b7730e741d0989f8e3e06e11935
        for lay in range(3):
            if self.map_enemy[lay, self.y, self.x] != 9 and self.map_enemy[lay, self.y, self.x] != 8:
                if resultShoot != 0:
                    self.map_enemy[lay, self.y, self.x] = 9
                    self.touch = True
                else:
                    self.map_enemy[lay, self.y, self.x] = 8
                self.TargetQMl.emit(self.x, self.y, lay, self.touch)
                break