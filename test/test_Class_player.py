# essayer de mettre une valeur en dehors de 0 et 15 voir s'il y a une 
from program.Class_player import player

def test_cleanBoat():
    pl = player()
    pl.map_allied[1, 5, 8] = 1
    pl.cleanBoat(5,5,8,8,1,1)
    assert pl.map_allied[1, 5, 8] == 0