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

from Frame import (
    run_window,
    WriteMsgRcv,
    addClient,
    removeClient,
    set_flag_list,
)
from client import connectClient, ClientSend, exitClient


status = Queue(maxsize=0)
statusclient = Queue(maxsize=0)


def running():
    """Run of the main thread."""
    statusConnect = 0
    while 1:
        if not statusclient.empty():
            receive_client = statusclient.get()
            print("Sys msg from Client: ", receive_client)
            if receive_client[0] == "rcv":
                print("receive_client: ", receive_client[1])
                WriteMsgRcv(receive_client[1])
            elif receive_client[0] == "Connclient":
                addClient(receive_client[1])
            elif receive_client[0] == "list_rcv":
                set_flag_list()
            elif receive_client[0] == "Discoclient":
                removeClient(receive_client[1])

        elif not status.empty():
            dataReceive = status.get()
            print("Sys msg from Frame: ", dataReceive)

            if dataReceive[0] == "Connect":
                print("Start processus client")
                statusclient.put(
                    ["RunClient", dataReceive[1], dataReceive[2]], True,
                )
                statusConnect = 1
            elif dataReceive[0] == "Pseudo":
                ClientSend(11, dataReceive[1])

            elif dataReceive[0] == "text" and statusConnect == 1:
                ClientSend(7, dataReceive[1])
            elif dataReceive[0] == "text" and statusConnect == 0:
                print(
                    "Try to send data but not connected to server at ",
                    datetime.datetime.now(),
                )

            if dataReceive == "exit":
                if statusConnect == 1:
                    ClientSend(99, "")
                exitClient()
                print("Main close")
                break
        else:
            time.sleep(0.1)


thread1 = threading.Thread(target=running, args=())
thread1.start()
thread2 = threading.Thread(target=connectClient, args=(statusclient,))
thread2.start()

run_window(status)

# Closing
thread1.join()
thread2.join()
status.close()
statusclient.close()

# Sous Windows il faut mettre ce programme en pause (inutile sous Linux)
# os.system("pause")

print("All threads close")
