from program.LogicGame.Class_player import player

def test_init_player():
    pl = player()
    assert pl.size_x == 15
    assert pl.size_y == 15
    assert pl.layer == 2

def test_TestPlaceBoat():
    pl = player()
    pl.TestPlaceBoat(1,1,1,0,0)
    assert pl.x_finish == 6
    assert pl.y_finish == 3
    #pl.TestPlaceBoat(1,1,2,1,1)
    #assert pl.x_finish == 5
    #assert pl.y_finish == 2
    #pl.TestPlaceBoat(1,1,3,1,1)
    #assert pl.x_finish == 6
    #assert pl.y_finish == 2
    #pl.TestPlaceBoat(1,1,4,1,1)
    #assert pl.x_finish == 5
    #assert pl.y_finish == 2
   