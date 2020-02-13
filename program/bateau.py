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
    def __init__(self, size_x=5, size_y=2, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class Destroyer:
    def __init__(self, size_x=4, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class PA:
    def __init__(self, size_x=5, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class Tor:
    def __init__(self, size_x=4, size_y=1, layer=1):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer

