
from program.Class_Map import Map
from program.bateau import Boat
from program.sous_marin import SM
from program.sous_marin import SM, SMNuclear, PSM, MSM
from program.bateau import Boat, Container, Destroyer, PA, Tor

class player:
    def __init__(self):
        self.name = ""
        self.map = Map()
        self.container = Container()
        self.pa = PA()
        self.destroyer = Destroyer()
        self.tor = Tor()
        self.PSM_1 = PSM()
        self.MSM_1 = MSM()
        self.SMNuclear_1 = SMNuclear()
