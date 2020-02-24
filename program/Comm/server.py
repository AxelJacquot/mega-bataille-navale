from PySide2.QtCore import QObject, Slot
import os
import time

class server(QObject):

    def __init__(self):
        super(server,self).__init__()

    @Slot(str, str)
    def startServer(self, ip, port):
        cmd = 'python program/Comm/chat_server.py ' + ip + ' ' + port
        os.popen(cmd)
        time.sleep(0.01)