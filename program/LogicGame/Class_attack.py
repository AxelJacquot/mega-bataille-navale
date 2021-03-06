import numpy as np

from PySide2.QtCore import QObject, Slot, Signal


class Attack(QObject):
    

    TargetShoot = Signal(int, int, int)
    Target = Signal()
    TargetQMl = Signal(int, int, int, bool, bool)

    def __init__(self):
        super(Attack, self).__init__()
        self.map_enemy = np.zeros(225 * 3)
        self.map_enemy.resize((3, 15, 15))
        self.touch = False
        self.x = 0
        self.y = 0
        self.tir = 0

    @Slot(int, int, result=bool)
    def tire(self, x, y):
        print("Tire")
        print(x, y)
        error = False
        if self.map_enemy[0, y, x] == 9 or self.map_enemy[0, y, x] == 8:
            if self.map_enemy[1, y, x] == 9 or self.map_enemy[1, y, x] == 8:
                if self.map_enemy[2, y, x] == 9 or self.map_enemy[2, y, x] == 8:
                    print(error)
                    error = True
        if(error == False):
            # fonction envoie et attente de reponse
            self.x = x
            self.y = y
            x += 1
            y += 1
            self.TargetShoot.emit(2 ,x, y)
            #self.Target.emit()
        print(error)
        return error

    @Slot(int, int)
    def tire2(self, resultShoot, coule):
        self.touch = False
        for lay in range(3):
            if self.map_enemy[lay, self.y, self.x] != 9 and self.map_enemy[lay, self.y, self.x] != 8:
                if resultShoot != 0:
                    self.map_enemy[lay, self.y, self.x] = 9
                    self.touch = True
                    if coule != 0:
                        self.TargetQMl.emit(self.x, self.y, lay, self.touch, True)
                    else:
                        self.TargetQMl.emit(self.x, self.y, lay, self.touch, False)
                else:
                    self.map_enemy[lay, self.y, self.x] = 8
                    self.touch = False
                    self.TargetQMl.emit(self.x, self.y, lay, self.touch, False)
            if(self.touch == True):
                break
        
