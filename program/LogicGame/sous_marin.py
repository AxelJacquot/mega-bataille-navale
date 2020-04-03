class SMNuclear:
    def __init__(self, size_x=6, size_y=1, layer=2):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def place_boat(self, x, y, type_boat, index, orientation):
        if type_boat == 5:
            if 2 > index >= 0:
                if orientation == 1:
                    if x + self.size_y <= 15 and (y >= 0) and (x >= 0) and y + self.size_x <= 15:
                        self.x_finish = x + self.size_y
                        self.y_finish = y + self.size_x
                        return True
                    else:
                        return False
                elif orientation == 0:
                    if x + self.size_x <= 15 and (y >= 0) and (x >= 0) and y + self.size_y <= 15:
                        self.x_finish = x + self.size_x
                        self.y_finish = y + self.size_y
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

class PSM:
    def __init__(self, size_x=3, size_y=1, layer=2):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def place_boat(self, x, y, type_boat, index, orientation):
        if type_boat == 6:
            if 5 > index >= 0:
                if orientation == 1:
                    if x + self.size_y <= 15 and (y >= 0) and (x >= 0) and y + self.size_x <= 15:
                        self.x_finish = x + self.size_y
                        self.y_finish = y + self.size_x
                        return True
                    else:
                        return False
                elif orientation == 0:
                    if x + self.size_x <= 15 and (y >= 0) and (x >= 0) and y + self.size_y <= 15:
                        self.x_finish = x + self.size_x
                        self.y_finish = y + self.size_y
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False


class MSM:
    def __init__(self, size_x=2, size_y=1, layer=2):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def place_boat(self, x, y, type_boat, index, orientation):
        if type_boat == 7:
            if 2 > index >= 0:
                if orientation == 1:
                    if x + self.size_y <= 15 and (y >= 0) and (x >= 0) and y + self.size_x <= 15:
                        self.x_finish = x + self.size_y
                        self.y_finish = y + self.size_x
                        return True
                    else:
                        return False
                elif orientation == 0:
                    if x + self.size_x <= 15 and (y >= 0) and (x >= 0) and y + self.size_y <= 15:
                        self.x_finish = x + self.size_x
                        self.y_finish = y + self.size_y
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
