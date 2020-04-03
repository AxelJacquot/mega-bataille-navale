import socket
from PySide2.QtCore import QObject, Signal, Slot, Property, QThread

class Reseau(QThread):

    playerConnected = Signal(str)
    ReceiveShoot = Signal(int, int)
    SendShoot = Signal(int, int)
    Connect = Signal()
    
    def __init__(self):
        QThread.__init__(self, parent=None)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.isclient = True
        self.existing = False
        self.messageReceive = ""

    @Slot(str, str, result=int)
    def client(self, ip, port):
        port = int(port)
        client = (ip, port)
        error = False
        try:
            self.socket.connect(client)
        except:
            error = True
        if error == False:
            print("Good Connect")
            self.Connect.emit()
            return 1
        else:
            print("Bad Connect")
            return 0

    @Slot(str, str, result=int)
    def host(self, ip, port):
        port = int(port)
        error = False
        host = (ip, port)
        try:
            self.socket.bind(host)
        except:
            error = True
            print("Connexion Impossible")
            return 0
        if error == False:
            self.isclient = False
            self.socket.listen(2)
            self.socketServeur, self.infos_connexion = self.socket.accept()
            print(self.infos_connexion)
            self.Connect.emit()
            return 1

    @Slot(int, str)
    def sendPseudo(self, code, message):
        bytemessage = ""
        bytemessage += chr(code)
        bytemessage += chr(len(message))
        bytemessage += message
        print("Message: ", message, "\n\r Bytemessage: ", bytemessage)
        if self.isclient:
            self.socket.send(bytemessage.encode())
        else:
            self.socketServeur.send(bytemessage.encode())

    @Slot(int, int, int)
    def sendData(self, code, data1, data2):
        bytemessage = ""
        bytemessage += chr(code)
        bytemessage += chr(data1)
        bytemessage += chr(data2)
        print("Bytemessage: ", bytemessage)
        if self.isclient:
            self.socket.send(bytemessage.encode())
        else:
            self.socketServeur.send(bytemessage.encode())
        
    def run(self):
        while self.existing == False:
            if self.isclient:
                self.messageReceive = self.socket.recv(1024).decode()
            else:
                self.messageReceive = self.socketServeur.recv(1024).decode()
            #print(self.messageReceive)
            iD = ord(self.messageReceive[0])
            if iD == 1:
                lenght = ord(self.messageReceive[1])
                print(lenght)
                self.message = ""
                for i in range(lenght):
                    print(i)
                    self.message += self.messageReceive[i + 2]
                print(iD , lenght, self.message)
                self.playerConnected.emit(self.message)
            elif iD == 2:
                x = ord(self.messageReceive[1]) - 1
                y = ord(self.messageReceive[2]) - 1
                print(x, y)
                self.ReceiveShoot.emit(x, y)
            elif iD == 3:
                resultShoot = ord(self.messageReceive[1])
                sunk = ord(self.messageReceive[2])
                self.SendShoot.emit(resultShoot, sunk)
            else:
                print("Error iD")
