from reseau import Reseau
from PySide2.QtCore import Slot

@Slot(str)
def test(pseudo):
    print(pseudo)

if __name__ == "__main__":
    client = Reseau()
    client.client("192.168.43.236", 54546)
    while True:
        client.receiveData()
        