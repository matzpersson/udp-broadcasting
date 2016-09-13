##
##  broadcast.py
##  Udp Broadcase Example
##
##  Created by Matz Persson on 13/09/2011.
##  Copyright 2016 Headstation. All rights reserved.  It is free software and may be redistributed under the terms specified in the LICENSE file (Apache License 2.0). 
##

import os
import sys
import time
import hTools
import random
import socket

## -- Broadcast to everyone on port 54545
broadcast_address = '172.16.1.255'
broadcast_port = 54545
host = socket.gethostbyname(socket.getfqdn())

level_name = 'info' 
logfile_prefix = None
logger = hTools.initLogging(logfile_prefix, level_name, 'udp_broadcast')

logger.info('## -------------------------------------------------- ##') 
logger.info('## STARTING Headstation UDP Broadcast daemon -------- ##') 
logger.info('## -------------------------------------------------- ##') 
logger.info('Broadcast from ' + host + ':' + str(broadcast_port) + ' to ' + broadcast_address + ":" + str(broadcast_port) )

## -- Configure for broadcast
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

## -- Never ending
logger.info('Start Loop. Ctrl-C to end...' ) 

while True:

	## -- Set random sleep
	wait = random.randrange(1,10)

	msg = "Hello, I am THE Server and now... I must random sleep for " + str(wait) + " seconds."
	logger.info('... Sending: ' + msg) 
	s.sendto(msg, (broadcast_address, broadcast_port))

	time.sleep(wait)
