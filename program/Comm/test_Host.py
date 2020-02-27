from reseau import Reseau
from time import sleep

if __name__ == "__main__":
    host = Reseau()
    host.host("192.168.43.236", 54546)
    while True:
        host.sendData(2, 13, 14)
        sleep(10)
