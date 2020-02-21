import sys

from pprint import pprint
from program.Class_attack import Attack
from program.Class_player import player
from program.Class_defend import defend

from PySide2.QtCore import QObject, Signal, Property
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtQml import QQmlApplicationEngine   

if __name__ == "__main__":
    x = 0
    y = 0
    layer = 0
    player1 = player()
    defense = defend()
    attac = Attack()

    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    # Expose the Python object to QML
    context = engine.rootContext()
    context.setContextProperty("Attack", attac)
    context.setContextProperty("Defense", defense)
    context.setContextProperty("Player", player1)

    engine.load("GUI/main.qml")
    sys.exit(app.exec_())
