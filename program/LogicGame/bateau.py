class Container:
    def __init__(self, size_x=5, size_y=2, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def place_boat(self, x, y, type_boat, index, orientation):
        if type_boat == 1:
            if 1 > index >= 0:
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


class Destroyer:
    def __init__(self, size_x=4, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def place_boat(self, x, y, type_boat, index, orientation):
        if type_boat == 2:
            if 3 > index >= 0:
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


class PA:
    def __init__(self, size_x=5, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def place_boat(self, x, y, type_boat, index, orientation):
        if type_boat == 3:
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


class Tor:

    def __init__(self, size_x=3, size_y=2, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def place_boat(self, x, y, type_boat, index, orientation):
        if type_boat == 4:
            if 3 > index >= 0:
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

# num_sm
# 1 => porte-container
# 2 => porte-avion
# 3 => destroyer
# 4 => torpilleur
# 5 => sous-marin
# 6 => petit-sous-marin
# 7 => mini-sous-marin
# Orientation => 1 => Horizontale
# Orientation => 0 => Verticale
