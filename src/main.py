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

import threading
import time
import datetime
from multiprocessing import Queue
from PySide2.QtCore import Signal, Slot, QObject

from client import Client


status = Queue(maxsize=0)
statusclient = Queue(maxsize=0)


@Slot(str)
def print_pseudo(pseudo):
    print("Pseudo recu:", pseudo)


if __name__ == "__main__":
    """Run of the main thread."""
    statusconnect = 0

    # Tread client
    data_q = statusclient
    thread1 = Client(data_q)
    thread1.start()
    thread1.signal_pseudo.connect(print_pseudo)
    ip = "10.33.1.246"
    port = 5454
    pseudo = "Michel"
    thread1.connect(ip, port, pseudo)

    while 1:
        # interface code client
        if not statusclient.empty():
            receive_client = statusclient.get()
            print("Sys msg from Client: ", receive_client)
            if receive_client[0] == "rcv":
                print("receive_client message: ", receive_client[1])
                ####
            elif receive_client[0] == "Connclient":
                print("New client connect", receive_client[1])
                ####

        # interface code window
        elif not status.empty():
            data_receive = status.get()
            print("Sys msg from Frame: ", data_receive)

            # ask connection
            if data_receive[0] == "Connect":
                # data_receive: IP, Port, Pseudo
                print("Start processus client")
                statusclient.put(
                    ["Connect", data_receive[1], data_receive[2]],
                    data_receive[3],
                    True,
                )
                statusconnect = 1

            elif data_receive[0] == "text" and statusconnect == 1:
                Client.clientsend(7, data_receive[1])
            elif data_receive[0] == "text" and statusconnect == 0:
                print(
                    "Try to send data but not connected to server at ",
                    datetime.datetime.now(),
                )

            if data_receive == "exit":
                Client.exitclient()
                print("Main close")
                break
        else:
            time.sleep(0.1)

    # Closing
    thread1.join()
    status.close()
    statusclient.close()

# Sous Windows il faut mettre ce programme en pause (inutile sous Linux)
# os.system("pause")

print("All threads close")
