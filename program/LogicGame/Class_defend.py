from program.LogicGame.Class_player import player, map_allied, boat
from PySide2.QtCore import QObject, Signal, Property, Slot

class defend(QObject):

    ShootQML = Signal(int, int, int, bool)
    Shoot = Signal(int, int, int)

    def __init__(self):
        super(defend,self).__init__()
        self.touch = 0



    @Slot(int, int)
    def case_tire(self, x, y):
        print("Defense Case")
        print(x ,y)
        data1 = 0
        data2 = 0
        xSize = 0
        ySize = 0
        touche = 0
        layer = 0
        errorCoule = 0
        for lay in range(3):
            if map_allied[lay, y, x] != 0 and map_allied[lay, y, x] != 9 and map_allied[lay, y, x] != 8:
                test = 1
                typeBoat = int(map_allied[lay, y, x])
                if lay == 0:
                    if typeBoat == 1 or typeBoat == 2 or typeBoat == 3 or typeBoat == 4:
                        data1 = 1
                    else:
                        data1 = 2
                else:
                    data1 = 3

                for i in range(5):
                    test = boat[typeBoat][i]
                    if test[0] >= x <= test[1] and test[2] >= y <= test[3] and lay == test[4]:
                        xSize = int(test[0] - test[1] + 1)
                        ySize = int(test[2] - test[2] + 1)
                        for xCoule in range(int(test[0]), int(test[1])):
                            for yCoule in range(int(test[2]), int(test[3])):
                                if map_allied[lay, yCoule, xCoule] == 9:
                                    errorCoule += 1
                        if (xSize * ySize) == errorCoule  and errorCoule != 0:
                            data2 = 1
                        break
                layer = lay
                touche = 1
                map_allied[lay, y, x] = 9
                break
            elif map_allied[lay, y, x] == 0:
                layer = lay
                touche = 0
                map_allied[lay, y, x] = 8
                break
        self.ShootQML.emit(x, y, layer, touche)
        self.Shoot.emit(3, data1, data2)
        

# num_sm
# 1 => porte-container
# 2 => porte-avion
# 3 => destroyer
# 4 => torpilleur
# 5 => sous-marin
# 6 => petit-sous-marin
# 7 => mini-sous-marin

