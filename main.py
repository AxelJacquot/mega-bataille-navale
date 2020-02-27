import sys
import threading
import time
import datetime
from multiprocessing import Queue

from pprint import pprint
from program.LogicGame.Class_attack import Attack
from program.LogicGame.Class_player import player , boat
from program.LogicGame.Class_defend import defend
from program.Comm.reseau import Reseau
from PySide2.QtCore import QObject, Signal, Property
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtQml import QQmlApplicationEngine

if __name__ == "__main__":

    player1 = player()
    defense = defend()
    attack = Attack()
    reseau = Reseau()

    attack.TargetShoot.connect(reseau.sendData)
    attack.Target.connect(reseau.receiveData)

    defense.Shoot.connect(reseau.sendData)

    reseau.ReceiveShoot.connect(defense.case_tire)
    reseau.SendShoot.connect(attack.tire2)

    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    # Expose the Python object to QML
    context = engine.rootContext()
    context.setContextProperty("Attack", attack)
    context.setContextProperty("Defense", defense)
    context.setContextProperty("Player", player1)
    context.setContextProperty("Reseau", reseau)
    engine.load("GUI/main.qml")
    sys.exit(app.exec_())

    # exit client

