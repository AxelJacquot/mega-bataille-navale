import numpy as np

from PySide2.QtCore import QObject, Slot, Signal

class Attack(QObject):
    touch = 0

    TargetShoot = Signal(int, int, int)
    Target = Signal()
    TargetQMl = Signal(int, int, int, bool)

    def __init__(self):
        super(Attack,self).__init__()
        self.map_enemy = np.zeros(225 * 3)
        self.map_enemy.resize((3, 15, 15))
        self.x = 0
        self.y = 0
        self.tir = 0

    @Slot(int, int)
    def tire(self, x, y):
        print(x, y)
        # fonction envoie et attente de reponse
        self.x = x
        self.y = y
        x += 1
        y += 1
        self.TargetShoot.emit(2 ,x, y)
        self.Target.emit()

    @Slot(int, int)
    def tire2(self, resultShoot, coule):
        touch = False
        for lay in range(3):
            if self.map_enemy[lay, self.y, self.x] != 9 and self.map_enemy[lay, self.y, self.x] != 8:
                if resultShoot != 0:
                    self.map_enemy[lay, self.y, self.x] = 9
                    touch = True
                else:
                    self.map_enemy[lay, self.y, self.x] = 8
                self.TargetQMl.emit(self.x, self.y, lay, touch)
                break
