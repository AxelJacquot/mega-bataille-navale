from program.LogicGame.Class_defend import defend
from program.LogicGame.Class_player import player, map_allied


df = defend()


def test_case_tire_1():

    map_allied[2, 6, 5]= 5
    assert df.case_tire_1(5,6,2,1)==1
    map_allied[2, 6, 5]= 0
    assert df.case_tire_1(5,6,2,1)== 0