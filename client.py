# -------------------------------------------------------------------------------
# Name:        ArchiComm
# Purpose:
#
# Author:      Thomas
#
# Created:     11/01/2020
# Copyright:   (c) Thomas 2020
# Licence:     <>
# -------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
# !/usr/bin/env python

import socket
import simplelogging
from PySide.QtCore import Signal, Slot

log = simplelogging.get_logger()
status_client = False


class Client:
    """Make interface TPC client workable by a main code."""

    signal = Signal()
    status_client = False

    def liveofclient(self, data_q):
        """Life of all the client."""
        print("Client ok")
        global client_socket
        global status_client
        status_client = True
        data_rcv = ""
        data_receive = []
        message = ""
        success = False

        # process connection
        while status_client:
            if not data_q.empty():
                success = self.tryconnection(data_q)
                if success:
                    break
                else:
                    log.error("connect fail")

        # process connection done, life of communication
        while status_client:
            try:
                data_rcv = client_socket.recv(2048)
            except OSError:
                pass  # no data receive
            if data_rcv:
                # message = data_rcv.decode()
                ID = data_rcv[0]
                lenght = data_rcv[1]
                print("ID receive:", data_rcv[0])
                print("lenght receive:", data_rcv[1])
                for i in range(lenght + 1):
                    message += chr(data_rcv[i + 2])
                message = message[1:]
                print("Message rcv:", message)

                # receive new client connect in game
                if ID == 1:
                    pseudos = message.split(",")
                    for pseudo in pseudos:
                        if pseudo != "":
                            print("pseudo[", i, "]=", pseudo)
                            data_q.put(["Connclient", pseudo])
                    message = ""
                elif ID == 2:
                    print("Reception attack")
                elif ID == 3:
                    print("Reception reponce attack")
                # receive new classique message
                elif ID == 5:
                    data_q.put(["rcv", message, ""], True)
                    message = ""
                data_rcv = False
        client_socket.close()
        print("Client close")

    def tryconnection(self, data_q):
        data_receive = data_q.get(False)
        if data_receive[0] == "RunClient":
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.setblocking(0)
            client_socket.settimeout(10)
            ip_address = data_receive[1]
            port = data_receive[2]
            pseudo = data_receive[3]
            catcherror = 0

            try:
                client_socket.connect((ip_address, port))

            except socket.gaierror as e:
                print(
                    "Address-related error connecting to CLIENT: ",
                    e,
                    " Fail to connect to: ",
                    ip_address,
                    port,
                )
                catcherror = 1

            except OSError as e:
                print(
                    "Connection error: ",
                    e,
                    " Fail to connect to: ",
                    ip_address,
                    port,
                )
                catcherror = 1

            if catcherror == 0:
                self.clientsend(1, pseudo)
                print("We are CONNECT")
                return True
            else:
                print("error has catch")

    def clientsend(self, code: int, data: str):
        """Send data to server."""
        global client_socket
        bytesmsg = bytearray(3)
        bytesmsg[0] = code
        bytesmsg[1] = len(data)
        bytesmsg.extend(data.encode())
        print("data:", data, " bytesmsg:", bytesmsg)
        client_socket.send(bytesmsg)

    # replacemultiple(list[i], ["[", "]", '"', "'"], "")
    def replacemultiple(self, mainstring, be_renplace, newstring):
        """Iterate over the strings to be replaced."""
        for elem in be_renplace:
            # Check if string is in the main string
            if elem in mainstring:
                # Replace the string
                mainstring = mainstring.replace(elem, newstring)
        return mainstring

    def exitclient(self):
        """Desactive main function of the client (liveofclient)."""
        global status_client
        status_client = False
