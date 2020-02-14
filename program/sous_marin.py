class SM:
    def __init__(self):
        self.PSM_1 = PSM()
        self.MSM_1 = MSM()
        self.SMNuclear_1 = SMNuclear()



class SMNuclear:
    def __init__(self, size_x=0, size_y=0, layer=2):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def place_boat(self, x , y, type_boat,index, orientation):
        if type_boat == 5:
            if 0 >= index < 2:
                if orientation == 1:
                    if  x <= x-self.size_y:
                        self.x_finish = x + self.size_y
                        self.y_finish = y + self.size_x
                    else:
                        return 1
                else:
                    if  x <= x-self.size_x:
                        self.x_finish = x + self.size_x
                        self.y_finish = y + self.size_y
                    else: 
                        return 1
            else:
                return 1

class PSM:
    def __init__(self, size_x=3, size_y=1, layer=2):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def place_boat(self, x , y, type_boat,index, orientation):
        if type_boat == 6:
            if 0 >= index < 3:
                if orientation == 1:
                    if  x <= x-self.size_y:
                        self.x_finish = x + self.size_y
                        self.y_finish = y + self.size_x
                    else:
                        return 1
                else:
                    if  x <= x-self.size_x:
                        self.x_finish = x + self.size_x
                        self.y_finish = y + self.size_y
                    else:
                        return 1
            else:
                return 1
        
                        

class MSM:
    def __init__(self, size_x=2, size_y=1, layer=2):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def place_boat(self, x , y, type_boat,index, orientation):
        if type_boat == 7:
            if 0 >= index < 2:
                if orientation == 1:
                    if  x <= x-self.size_y:
                        self.x_finish = x + self.size_y
                        self.y_finish = y + self.size_x
                    else:
                        return 1
                else:
                    if  x <= x-self.size_x:
                        self.x_finish = x + self.size_x
                        self.y_finish = y + self.size_y
                    else: 
                        return 1
            else:
                return 1