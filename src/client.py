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
from PySide2.QtCore import SIGNAL, QObject


status_client = False


def connectClient(data_q):
    """Life of all the client."""
    print("Client ok")
    global CLIENT
    global status_client
    status_client = True
    data_rcv = ""
    data_receive = []
    message = ""

    # process connection
    while status_client:
        if not data_q.empty():
            data_receive = data_q.get(False)

            if data_receive[0] == "RunClient":
                CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                CLIENT.setblocking(0)
                CLIENT.settimeout(10)
                ip_address = data_receive[1]
                port = data_receive[2]
                pseudo = data_receive[3]
                # pseudo = data_receive[3]
                catcherror = 0

                try:
                    CLIENT.connect((ip_address, port))

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
                    ClientSend(1, pseudo)
                    print("We are CONNECT")
                    break
                else:
                    print("error has catch")

    # process connection done, life of communication
    while status_client:
        try:
            data_rcv = CLIENT.recv(2048)
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
                print("pseudos:", pseudos)
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
    CLIENT.close()
    print("Client close")


def ClientSend(code: int, data: str):
    """Send data to server."""
    global CLIENT
    bytesmsg = bytearray(3)
    bytesmsg[0] = code
    bytesmsg[1] = len(data)
    bytesmsg.extend(data.encode())
    print("data:", data, " bytesmsg:", bytesmsg)
    CLIENT.send(bytesmsg)


# replaceMultiple(list[i], ["[", "]", '"', "'"], "")
def replaceMultiple(mainString, toBeReplaces, newString):
    """Iterate over the strings to be replaced."""
    for elem in toBeReplaces:
        # Check if string is in the main string
        if elem in mainString:
            # Replace the string
            mainString = mainString.replace(elem, newString)
    return mainString


def exitClient():
    """Desactive main function of the client (connectClient)."""
    global status_client
    status_client = False
