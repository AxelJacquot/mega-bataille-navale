from program.Class_defend import defend
from program.Class_player import player

df = defend()
pl = player(0,1,0,1,1)

def test_case_tire_1():
    assert df.case_tire_1(0,0,0,pl,1)==0


def test_case_tire_1():
    assert df.case_tire_1(0,0,0,pl,2)== None