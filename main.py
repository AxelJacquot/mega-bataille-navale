import sys
import threading
import time
import datetime
from multiprocessing import Queue

from pprint import pprint
from program.LogicGame.Class_attack import Attack
from program.LogicGame.Class_player import player
from program.LogicGame.Class_defend import defend
from program.Comm.client import Client
from PySide2.QtCore import QObject, Signal, Property
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtQml import QQmlApplicationEngine

status = Queue(maxsize=0)
statusclient = Queue(maxsize=0)

if __name__ == "__main__":
    x = 0
    y = 0
    layer = 0
    player1 = player()
    defense = defend()
    attac = Attack()

    # ########### part Comm TCP ###########
    statusconnect = 0
    data_q = statusclient
    thread1 = Client(data_q)
    thread1.start()
    """
        thread1.signal_pseudo.connect(print_pseudo)
        ip = "10.33.1.246"
        port = 5454
        pseudo = "Michel"
        thread1.connect(ip, port, pseudo)
    """
    # ########### end config Comm TCP ###########

    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    # Expose the Python object to QML
    context = engine.rootContext()
    context.setContextProperty("Attack", attac)
    context.setContextProperty("Defense", defense)
    context.setContextProperty("Player", player1)
    engine.load("GUI/main.qml")
    sys.exit(app.exec_())

    # exit client
    Client.exitclient()
    thread1.join()
    status.close()
    statusclient.close()
