class SM:
    def __init__(self):
        self.PSM_1 = PSM()
        self.PSM_2 = PSM()
        self.PSM_3 = PSM()
        self.PSM_4 = PSM()
        self.PSM_5 = PSM()

        self.MSM_1 = MSM()
        self.MSM_2 = MSM()

        self.SMNuclear_1 = SMNuclear()
        self.SMNuclear_2 = SMNuclear()


class SMNuclear:
    size_x = None
    size_y = None

    def __init__(self, size_x=0, size_y=0, layer=2):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class PSM:
    size_y = None
    size_x = None

    def __init__(self, size_x=3, size_y=1, layer=2):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


class MSM:
    size_x = None
    size_y = None

    def __init__(self, size_x=2, size_y=1, layer=2):
        self.size_x = size_x
        self.size_y = size_y
        self.layer = layer


