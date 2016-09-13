##
##  client.py
##  Udp Broadcast Client Listen Example
##
##  Created by Matz Persson on 13/09/2011.
##  Copyright 2016 Headstation. All rights reserved.  It is free software and may be redistributed under the terms specified in the LICENSE file (Apache License 2.0). 
##

import os
import sys
import hTools
import socket

## -- Receive any 172.16.1.* UDP broadcast on port 54545
UDP_IP = "172.16.1.255"
UDP_PORT = 54545

## -- Start logging
level_name = 'info' 
logfile_prefix = None
logger = hTools.initLogging(logfile_prefix, level_name, 'udp_client')

logger.info('## --------------------------------------------------------- ##') 
logger.info('## STARTING Headstation UDP Broadcast Client Listen -------- ##') 
logger.info('## --------------------------------------------------------- ##') 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

## -- Bind port
sock.bind((UDP_IP, UDP_PORT))

logger.info('Listening on ' + UDP_IP + ':' + str(UDP_PORT)  )
while True:

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    logger.info('... Received from ' + addr[0] + " - Message: " + data)
