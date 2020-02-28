from program.LogicGame.Class_attack import Attack

def test_tire():
    at=Attack()
    at.tire(1,3)
    assert at.x == 1
    assert at.y == 3

def test_tire2():
    at=Attack()
    at.tire2(1,1)
    assert at.touch == True   



    


 