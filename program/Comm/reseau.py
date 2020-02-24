import socket
from PySide2.QtCore import QObject, Signal, Slot

class Reseau(QObject):

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.isclient = True
        self.messageReceive = ""

    @Signal
    def playerConnected(self):
        pass

    @Signal
    def SendTire(self):
        pass

    @Signal
    def ReceiveTire(self):
        pass

    @Slot(int, int, result=bool)
    def getCoorTire(self, x, y):
        pass


    @Slot(str, str)
    def client(self, ip, port):
        client = (ip, port)
        error = False
        try:
            self.socket.connect(client)
        except:
            error = True
        if error == False:
            print("Good Connect")
        else:
            print("Bad Connect")
        

    @Slot(str, str)
    def host(self, ip, port):
        self.isclient = False
        error = False
        host = (ip, port)
        try:
            self.socket.bind(host)
        except:
            error = True
            print("Use port already")
        if error == False:
            self.socket.listen(2)
            self.socketclient, self.infos_connexion = self.socket.accept()
            print(self.infos_connexion)

    @Slot(int, str)
    def sendData(self, code, message):
        bytemessage = bytearray(3)
        bytemessage[0] = code
        bytemessage[1] = len(message) + 1
        bytemessage.extend(message.encode())
        print("Message: ", message, "\n\r Bytemessage: ", bytemessage)
        if self.isclient:
            self.socket.send(bytemessage)
        else:
            self.socketclient.send(bytemessage)
        
    def receiveData(self):
        if self.isclient:
            self.messageReceive = self.socket.recv(1024)
        else:
            self.messageReceive = self.socketclient.recv(1024)

        iD = int(self.messageReceive[0])
        lenght = int(self.messageReceive[1])
        self.message = ""
        for i in range(lenght):
            self.message += chr(self.messageReceive[i + 2])
        print(iD , lenght, message)
        if iD == 1:
            self.playerConnected.emit()
        elif id == 2:
            self.ReceiveTire.emit()
        elif id == 3:
            self.SendTire.emit()
        else:
            print("Error iD")

    @Slot(result=QVariantList)
    def GetMessage(self):    
        return