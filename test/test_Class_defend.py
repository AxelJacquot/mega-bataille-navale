from program.LogicGame.Class_defend import defend
from program.LogicGame.Class_player import player, map_allied



def test_case_tire():
    df = defend()
    map_allied[2, 6, 5]= 5
    df.case_tire(5,6)
    assert df.touch == 1
    map_allied[2, 6, 5]= 0
    df.case_tire(5,6)
    assert df.touch == 0
    