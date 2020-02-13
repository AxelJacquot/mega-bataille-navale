from program.Class_attack import attack
from program.Class_player import player

def test_tire():
    at=attack()
    assert at.tire(1,5,2,1)==1
    assert at.tire(1,5,2,0)==0

def test_tire_x_case():
    at=attack()
    assert at.tire_x_case(1,5,2,0,4)==0
    at.tire_x_case(1,5,2,1,4)
    assert at.tir == 1
    
    
    


