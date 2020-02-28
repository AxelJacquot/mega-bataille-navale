from program.LogicGame.Class_player import player, map_allied, boat
from PySide2.QtCore import QObject, Signal, Property, Slot

class defend(QObject):

    ShootQML = Signal(int, int, int, bool, bool)
    Shoot = Signal(int, int, int)

    def __init__(self):
        super(defend,self).__init__()
        self.touch = 0
        self.layer = 0



    @Slot(int, int)
    def case_tire(self, x, y):
        print("Defense Case")
        print(x ,y)
        data1 = 0
        data2 = 0
        xSize = 0
        ySize = 0
        self.touch = 0
        self.layer = 0
        errorCoule = 0
        coule = False
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
                    xbegin = int(test[0])
                    xfinish = int(test[1])
                    ybegin = int(test[2])
                    yfinish = int(test[3])
                    layer = int(test[4])
                    if xbegin <= x <= xfinish  and ybegin <= y <= yfinish and lay == layer:
                        xSize = xbegin - xfinish + 1
                        ySize = ybegin - yfinish + 1
                        print("xSize: ", xSize)
                        print("ySize: ", ySize)
                        for xCoule in range(xbegin, xfinish):
                            for yCoule in range(ybegin, yfinish):
                                if ybegin <= y <= yfinish and xbegin <= x <= xfinish:
                                    if map_allied[lay, yCoule, xCoule] == 9:
                                        errorCoule += 1
                        if (xSize * ySize) == errorCoule  and errorCoule != 0:
                            data2 = 1
                            coule = True
                        break
                self.layer = lay
                print("test: ", self.layer)
                self.touch = 1
                map_allied[lay, y, x] = 9
                break
            elif map_allied[lay, y, x] == 0:
                self.layer = lay
                self.touch = 0
                map_allied[lay, y, x] = 8
        print("test: ", self.layer)
        self.ShootQML.emit(x, y, self.layer, self.touch, coule)
        self.Shoot.emit(3, data1, data2)
        

# num_sm
# 1 => porte-container
# 2 => porte-avion
# 3 => destroyer
# 4 => torpilleur
# 5 => sous-marin
# 6 => petit-sous-marin
# 7 => mini-sous-marin

