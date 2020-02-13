from program.Class_attack import attack
from program.Class_player import player

def test_tir(attack):
    player_test = player(6,5,7,9,5)
    assert attack.tire(1,4,2,player_test,1)==1

    