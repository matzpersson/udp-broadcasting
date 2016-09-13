# Python UDP Broadcasting
Python UDP Message Broadcasting on local network. Great for creating push driven messages to local applications. These are example scripts where the server sends the same message and random intervals. Client just listens and never pulls data.

# Installation
Fork or Download scripts into your directory. These scripts have been tested on python 2.* using Linux and OSX. Includes both example broadcast and client receiver scripts. Please note that both can not run on the same server at the same time as broadcast IP will clash.

# Configuration
In broadcast.py, change broadcast_address to suit your network. You can broadcast to specific client by nominating their ip address/port or broadcast on the whole network.
In our environment, the network mask is 255.255.255.0 and network is 172.16.1.0. To broadcast to everyone, we set the broadcast address in broadcast.py to either 172.16.1.255 or 255.255.255.255.

In client.py, change the UDP_IP address to be blank or broadcast address which in our case was 172.16.1.255. You can run this on as many clients as you like to receive random messages from the server.

# Usage
To start broadcast in terminal: python broadcast.py

To start clients in terminal: python client.py


# Copyright
Copyright 2016 Headstation. (http://headstation.com) All rights reserved.  It is free software and may be redistributed under the terms specified in the LICENSE file (Apache License 2.0). 
