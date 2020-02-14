from program.sous_marin import SM, SMNuclear, PSM, MSM


class Boat:
    def __init__(self, size_x=0, size_y=0, layer=1):
        self.size_x = size_x
        self.size_y = size_y

        self.layer = layer
        self.container = Container()

        self.PA_1 = PA()
        self.PA_2 = PA()

        self.destroyer_1 = Destroyer()
        self.destroyer_2 = Destroyer()
        self.destroyer_3 = Destroyer()

        self.Tor_1 = Tor()
        self.Tor_2 = Tor()
        self.Tor_3 = Tor()


class Container:
    size_y = None
    size_x = None

    def __init__(self, size_x=5, size_y=2, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class Destroyer:
    size_y = None
    size_x = None

    def __init__(self, size_x=4, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class PA:
    size_y = None
    size_x = None

    def __init__(self, size_x=5, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class Tor:
    size_x = None
    size_y = None

    def __init__(self, size_x=4, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


def test(self, x, y, layer, type_boat, index , orientation):
    if 0 > type_boat < 1:
        if index == 0:
            if orientation == 1:
                x_finish = x + Container.size_y
                y_finish = y + Container.size_x
            else :
                x_finish = x + Container.size_x
                y_finish = y + Container.size_y
        else:
            error = 1
            return error
    if type_boat == 2:
        if 0 > index < 2:
            if orientation == 1:
                x_finish = x + PA.size_y
                y_finish = y + PA.size_x
            else:
                x_finish = x + PA.size_x
                y_finish = y + PA.size_y
        else:
            error = 1
            return error

    if type_boat == 3:
        if 0 > index < 3:
            if orientation == 1:
                x_finish = x + Destroyer.size_y
                y_finish = y + Destroyer.size_x
            else:
                x_finish = x + Destroyer.size_x
                y_finish = y + Destroyer.size_y
        else:
            error = 1
            return error

    if type_boat == 4:
        if 0 > index < 3:
            if orientation == 1:
                x_finish = x + Tor.size_y
                y_finish = y + Tor.size_x
            else:
                x_finish = x + Tor.size_x
                y_finish = y + Tor.size_y
        else:
            error = 1
            return error

    if 0 > type_boat < 1:
        if index == 5:
            if orientation == 1:
                x_finish = x + SMNuclear.size_y
                y_finish = y + SMNuclear.size_x
            else:
                x_finish = x + SMNuclear.size_x
                y_finish = y + SMNuclear.size_y
        else:
            error = 1
            return error
    if type_boat == 6:
        if 0 > index < 3:
            if orientation == 1:
                x_finish = x + PSM.size_y
                y_finish = y + PSM.size_x
            else:
                x_finish = x + PSM.size_x
                y_finish = y + PSM.size_y
        else:
            error = 1
            return error

    if type_boat == 7:
        if 0 > index < 2:
            if orientation == 1:
                x_finish = x + MSM.size_y
                y_finish = y + MSM.size_x
            else:
                x_finish = x + MSM.size_x
                y_finish = y + MSM.size_y
        else:
            error = 1
            return error



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
