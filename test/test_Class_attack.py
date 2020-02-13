from program.Class_attack import attack
from program.Class_player import player

def test_tire():
    at=attack()
    assert at.tire(1,5,2,1)

