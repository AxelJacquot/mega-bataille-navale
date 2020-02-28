from program.LogicGame.bateau import Container, Destroyer, PA, Tor

def test_container():
    container = Container()
    assert container.size_x == 5
    assert container.size_y == 2
    assert container.layer == 1

def test_destroyer():
    destroyer = Destroyer()
    assert destroyer.size_x ==4
    assert destroyer.size_y == 1
    assert destroyer.layer == 1

def test_pa():
    pa = PA()
    assert pa.size_x == 5
    assert pa.size_y == 1
    assert pa.layer == 1


def test_tor():
    tor = Tor()
    assert tor.size_x == 4
    assert tor.size_y == 1
    assert tor.layer == 1