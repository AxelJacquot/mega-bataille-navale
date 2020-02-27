from reseau import Reseau
from PySide2.QtCore import Slot

@Slot(str)
def test(pseudo):
    print(pseudo)

if __name__ == "__main__":
    client = Reseau()
    client.client("10.33.1.159", 5454)
    client.playerConnected.connect(test)
    while True:
        client.receiveData()
        