# -------------------------------------------------------------------------------
# Name:        Mega bataille navale
# Purpose:     Student project
#
# Author:      Thomas
#
# Created:     11/01/2020
# Copyright:   (c) Thomas 2020
# Licence:     <>
# -------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
# !/usr/bin/env python
import mock
import socket
import threading
import simplelogging
from PySide2.QtCore import Signal, Slot, QObject
from PySide2 import *

log = simplelogging.get_logger()
status_client = False


class Client(QObject, threading.Thread):
    """Make interface TPC client workable by a main code."""
    
    signal_connect = Signal(bool)
    Signalpseudo = Signal(str)
    signal_shot = Signal(str)

    def __init__(self):
        super(Client, self).__init__()
        """Init the Thread of the Client."""
        threading.Thread.__init__(self)
        # self.ip_port = ip_port
        self.status_client = False
        self.data_rcv = ""
        self.data_receive = []
        self.message = ""
        self.success = False
        self.Signalpseudo = Signal(str)
        print("Init done")

    @Slot(str, str, str, )
    def connect(self, ip, port, pseudo):
        """Process connection."""
        self.status_client = True
        self.ip_address = str(ip)
        self.port = int(port)
        self.pseudo = str(pseudo)
        success = self.tryconnection()
        if success:
            log.info("Connection done, run client")
            self.life = threading.Thread(target=self.runClient, args=())
            self.life.start()
            #self.Signalpseudo(pseudo)
            return True
        else:
            log.error("Connect fail")
            return False

    def runClient(self):
        """Life of all the client."""
        # process connection done, life of communication
        while self.status_client:
            try:
                self.data_rcv = self.client_socket.recv(2048)
            except OSError:
                pass  # no data receive
            if self.data_rcv:
                # message = data_rcv.decode()
                self.ID = self.data_rcv[0]
                self.lenght = self.data_rcv[1]
                lenght = int(self.lenght)
                print("ID receive:", self.data_rcv[0])
                print("lenght receive:", self.data_rcv[1])
                for i in range(lenght + 1):
                    self.message += chr(self.data_rcv[i + 2])
                self.message = self.message[1:]
                
                print("Message rcv:", self.message)
                # receive new client connect in game
                if self.ID == 1:
                    self.pseudos = self.message.split(",")
                    for pseudo in self.pseudos:
                        if pseudo != "":
                            print("pseudo[", i, "]=", pseudo)
                            
                    message = ""
                elif ID == 2:
                    print("Reception attack", message)
                    message = ""
                elif ID == 3:
                    print("Reception reponce attack", message)
                    message = ""
                # receive new classique message
                elif ID == 5:
                    self.data_q.put(["rcv", self.message, ""], True)
                    self.message = ""
                data_rcv = False
        self.client_socket.close()
        print("Client close")

    def tryconnection(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.setblocking(0)
        self.client_socket.settimeout(10)
        catcherror = 0
        try:
            self.client_socket.connect((self.ip_address, self.port))
        except socket.gaierror as e:
            print(
                "Address-related error connecting to CLIENT: ",
                e,
                " Fail to connect to: ",
                self.ip_address,
                self.port,
            )
            catcherror = 1
        except OSError as e:
            print(
                "Connection error: ",
                e,
                " Fail to connect to: ",
                self.ip_address,
                self.port,
            )
            catcherror = 1
        if catcherror == 0:
            # send pseudo to the server
            self.clientsend(1, self.pseudo)
            print("We are CONNECT")
            return True
        else:
            print("error has catch")
            return False

    def clientsend(self, code: int, data: str):
        """Send data to server."""
        bytesmsg = bytearray(3)
        bytesmsg[0] = code
        bytesmsg[1] = len(data)
        bytesmsg.extend(data.encode())
        print("data:", data, " bytesmsg:", bytesmsg)
        self.client_socket.send(bytesmsg)

    @Slot()
    def exitclient(self):
        """Desactive main function of the client (liveofclient)."""
        self.status_client = False
