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

import threading
import time
import datetime
from multiprocessing import Queue

from client import connectClient, clientsend, exitclient


status = Queue(maxsize=0)
statusclient = Queue(maxsize=0)


def running():
    """Run of the main thread."""
    statusconnect = 0
    while 1:
        # interface code client
        if not statusclient.empty():
            receive_client = statusclient.get()
            print("Sys msg from Client: ", receive_client)
            if receive_client[0] == "rcv":
                print("receive_client message: ", receive_client[1])
                ####
            elif receive_client[0] == "Connclient":
                print("New client connect")
                ####

        # interface code window
        elif not status.empty():
            data_receive = status.get()
            print("Sys msg from Frame: ", data_receive)

            if data_receive[0] == "Connect":
                # data_receive: IP, Port, Pseudo
                print("Start processus client")
                statusclient.put(
                    ["RunClient", data_receive[1], data_receive[2]],
                    data_receive[3],
                    True,
                )
                statusconnect = 1
            elif data_receive[0] == "Pseudo":
                clientsend(11, data_receive[1])

            elif data_receive[0] == "text" and statusconnect == 1:
                clientsend(7, data_receive[1])
            elif data_receive[0] == "text" and statusconnect == 0:
                print(
                    "Try to send data but not connected to server at ",
                    datetime.datetime.now(),
                )

            if data_receive == "exit":
                exitclient()
                print("Main close")
                break
        else:
            time.sleep(0.1)


# Tread interface window
thread1 = threading.Thread(target=running, args=())
thread1.start()
# Tread client
thread2 = threading.Thread(target=connectClient, args=(statusclient,))
thread2.start()

# run interface window
run_window(status)

# Closing
thread1.join()
thread2.join()
status.close()
statusclient.close()

# Sous Windows il faut mettre ce programme en pause (inutile sous Linux)
# os.system("pause")

print("All threads close")
