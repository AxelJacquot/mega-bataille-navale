import socket
from PySide2.QtCore import QObject, Signal, Slot, Property

class Reseau(QObject):

    playerConnected = Signal(str)
    ReceiveShoot = Signal(int, int)
    SendShoot = Signal(int, int)

    ConnectClient = Signal(bool)
    ConnectHost = Signal(bool)
    
    def __init__(self):
        super(Reseau, self).__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.isclient = True
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
            return 1
            #self.ConnectClient.emit(True)
        else:
            print("Bad Connect")
            return 0
            self.ConnectClient.emit(False)

    @Slot(str, str, result=int)
    def host(self, ip, port):
        self.isclient = False
        port = int(port)
        error = False
        host = (ip, port)
        try:
            self.socket.bind(host)
        except:
            error = True
            print("Connexion Impossible")
            #self.ConnectHost.emit(False)
            return 0
        if error == False:
            self.socket.listen(2)
            self.socketclient, self.infos_connexion = self.socket.accept()
            print(self.infos_connexion)
            return 1
            #self.ConnectHost.emit(True)

    @Slot(int, str)
    def sendPseudo(self, code, message):
        bytemessage = ""
        bytemessage += str(code)
        bytemessage += str(len(message))
        bytemessage += message
        print("Message: ", message, "\n\r Bytemessage: ", bytemessage)
        if self.isclient:
            self.socket.send(bytemessage.encode())
        else:
            self.socketclient.send(bytemessage.encode())

    @Slot(int, int, int)
    def sendData(self, code, data1, data2):
        bytemessage = ""
        bytemessage += str(code)
        bytemessage += str(data1)
        bytemessage += str(data2)
        print("Message: ", data1 + data2, "\n\r Bytemessage: ", bytemessage)
        if self.isclient:
            self.socket.send(bytemessage.encode())
        else:
            self.socketclient.send(bytemessage.encode())
        
    @Slot()
    def receiveData(self):
        print("ici")
        if self.isclient:
            self.messageReceive = self.socket.recv(1024).decode()
        else:
            self.messageReceive = self.socketclient.recv(1024).decode()
        print("ici")
        iD = int(self.messageReceive[0])
        print(iD)
        if iD == 1:
            lenght = int(self.messageReceive[1])
            print(lenght)
            self.message = ""
            for i in range(lenght):
                print(i)
                self.message += self.messageReceive[i + 2]
            print(iD , lenght, self.message)
            self.playerConnected.emit(self.message)
        elif iD == 2:
            x = int(self.messageReceive[1]) - 1
            y = int(self.messageReceive[2]) - 1
            print(type(x))
            self.ReceiveShoot.emit(x, y)
        elif iD == 3:
            resultShoot = int(self.messageReceive[1])
            sunk = int(self.messageReceive[2])
            self.SendShoot.emit(resultShoot, sunk)
        else:
            print("Error iD")
