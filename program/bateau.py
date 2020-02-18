

class Boat:
    def __init__(self, size_x=0, size_y=0, layer=1):
        self.size_x = size_x
        self.size_y = size_y

        self.layer = layer
        self.container = Container()

        self.PA = PA()

        self.destroyer = Destroyer()
        self.Tor = Tor()


class Container:
    def __init__(self, size_x=5, size_y=2, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def place_boat(self, x , y, type_boat,index, orientation):
        if type_boat == 1:
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

class Destroyer:
    def __init__(self, size_x=4, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def place_boat(self, x , y, type_boat,index, orientation):
        if type_boat == 2:
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

class PA:
    def __init__(self, size_x=5, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0

    def place_boat(self, x , y, type_boat,index, orientation):
        if type_boat == 3:
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

class Tor:

    def __init__(self, size_x=4, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer
        self.x_finish = 0
        self.y_finish = 0
        
    def place_boat(self, x , y, type_boat,index, orientation):
        if type_boat == 4:
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
