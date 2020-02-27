from reseau import Reseau
from time import sleep

if __name__ == "__main__":
    host = Reseau()
    host.host("10.33.1.159", 5454)
    while True:
        host.sendPseudo(1,"Bonjour")
        sleep(10)
