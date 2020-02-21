#mettre des valeurs avec map_allied (valeurs random) si touchée avec 
# des valeurs différentes de 0 et tester touch
from program.Class_defend import defend
from program.Class_player import player, map_allied
import numpy as np

def test_case_tire_1():
    df = defend()

    map_allied[2, 2, 1] = 2 
    assert df.case_tire_1(1,2,2,1) == 1

    map_allied[2, 2, 1] = 0    
    assert df.case_tire_1(1,2,2,1) == 0
    
