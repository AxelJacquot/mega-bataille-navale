
class Map:
    def __init__(self, size_x=15, size_y=15, layer=2):
        self.error = -1
        self.map_allied = [[[0] * size_x] * size_y] * layer
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer

    def PSM(self, x_begin, x_finish, y_begin, y_finish, layer, num_sm):

        if 0 > x_begin < 15:
            return "x_begin case hors-map"
        elif 0 > x_finish < 15:
            return "x_ finish case hors-map"
        elif 0 > y_begin < 15:
            return "y_begin case hors-map"
        elif 0 > y_finish < 15:
            return "y_ finish case hors-map"
        elif 0 > layer < 3:
            return "couche hors de portée"
        else:
            for x in range(15):
                for y in range(15):
                    for lay in range(3):
                        if x_begin <= x <= x_finish and y_begin <= y <= y_finish and 0 <= lay <= layer:
                            if self.map_allied[x][y][lay] == 0:
                                if num_sm == 1:
                                    self.map_allied[x][y][lay] = 1
                                    return "ok"
                                if num_sm == 2:
                                    self.map_allied[x][y][lay] = 2
                                    return "ok"
                                if num_sm == 3:
                                    self.map_allied[x][y][lay] = 3
                                    return "ok"
                                if num_sm == 4:
                                    self.map_allied[x][y][lay] = 4
                                    return "ok"
                            else:
                                return "error : Case Prise"


