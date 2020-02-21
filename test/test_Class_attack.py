from program.Class_attack import attack

def test_tire():
    at=attack()
    at.map_enemy[1,8,5] = 5
    at.tire(5,8,1)
    assert at.map_enemy[1,8,5]==9
    


 
    


