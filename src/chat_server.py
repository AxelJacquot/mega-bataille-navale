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

"""Code server chatroom TCP."""

import socket
import threading
import sys
import time
import datetime
import simplelogging
from typing import List

log = simplelogging.get_logger()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
the first argument AF_INET is the address domain of the socket.
This is used when we have an Internet Domain with any two hosts.
The second argument is the type of socket. SOCK_STREAM means that
data or characters are read in a continuous flow
"""
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
print("Server is running")
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port))
# binds the server to an entered IP address and at the specified port number.
# The client must be aware of these parameters
server.listen(100)
# listens for 100 active connections.
# This number can be increased as per convenience
list_of_clients: List[socket.socket] = []
list_of_pseudo = []


def clientthread(conn, addr):
    """Control Main of the threads."""
    message = ""
    Pseudo = ""
    while True:
        try:
            data_rcv = conn.recv(2048)
            if data_rcv:
                ID = int(data_rcv[0])
                print("ID=", ID)
                lenght = int(data_rcv[1])
                message = ""
                for i in range(lenght):
                    message += chr(data_rcv[3 + i])
                if ID == 1:
                    Pseudo = treatmentConnection(conn, addr, message)
                elif ID == 2:
                    treatmentfire(conn, addr, 2, message)
                elif ID == 3:
                    treatmentreponcefire(conn, addr, 3, message)
                elif ID == 7:
                    treatmessage(conn, addr, Pseudo, message)
            """else:
                remove(conn)"""
        except:
            continue


def treatmentConnection(conn, addr, pseudo):
    """Treat new client connection."""
    lenght = 0
    log.info("<" + addr[0] + "> " + ": " + pseudo + " connected")
    # ##### send pseudo list to the new client ######
    bytesmsg = bytearray(3)
    bytesmsg[0] = 1
    if list_of_pseudo != []:
        for element in list_of_pseudo:
            lenght += len(element)
    bytesmsg[1] = lenght
    for pseudoelem in list_of_pseudo:
        pseudoelem = pseudoelem + ","  # add "," in the lenght of message
        bytesmsg[1] += 1
        bytesmsg.extend(bytearray(pseudoelem, "utf-8"))
    sendmsg(bytesmsg, conn, modebroadcast=False)
    list_of_pseudo.append(pseudo)
    log.info("List pseudo:%s", list_of_pseudo)
    # send the new pseudo to the other client
    bytesmsg = bytearray(3)
    bytesmsg[0] = 1
    lenght = len(pseudo)
    bytesmsg[1] = lenght
    bytesmsg[2] = pseudo
    sendmsg(bytesmsg, conn, modebroadcast=True)
    bytesmsg = bytearray(3)

    return pseudo


def treatmentfire(conn, addr, code, message):
    """Treat a shot."""
    bytesmsg = bytearray(3)
    bytesmsg[0] = code
    lenght = len(pseudo)
    bytesmsg[1] = lenght
    bytesmsg[2] = pseudo
    sendmsg(bytesmsg, conn, modebroadcast=True)


def treatmessage(conn, addr, Pseudo, message):
    """Treat sending message."""
    # prints the message and address of the user who just sent
    # the message on the server terminal
    print(
        datetime.datetime.now(),
        " ",
        "<" + addr[0] + "> " + Pseudo + ": " + message,
    )
    message_to_send = Pseudo + ": " + message
    bytesmsg = bytearray(3)
    bytesmsg[0] = 5
    bytesmsg[1] = len(message_to_send)
    bytesmsg.extend(map(ord, message_to_send))
    sendmsg(bytesmsg, conn, 1)


def sendmsg(message: bytearray, connection, modebroadcast):
    """Function to send message in broadcast or not."""
    # message = message.encode("utf8")
    # broadcast send to everyone expect transmitter
    for clients in list_of_clients:
        if modebroadcast:
            if clients != connection:
                try:
                    clients.send(message)
                except:
                    print(datetime.datetime.now(), " ", clients, " Leave")
                    clients.close()
                    remove(clients)
        elif clients == connection:  # mode private message
            print("MESSAGE SEND:", message)
            clients.send(message)
            break


def remove(connection):
    """Remove client connection of the list of connection."""
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    conn, addr = server.accept()
    """
    Accepts a connection request and stores two parameters, conn which is a socket object for that user, and addr which contains
    the IP address of the client that just connected
    """

    list_of_clients.append(conn)

    # maintains a list of clients for ease of broadcasting a message to all available people in the chatroom
    # Prints the address of the person who just connected
    threading._start_new_thread(clientthread, (conn, addr))
    # creates and individual thread for every user that connects

conn.close()
server.close()
