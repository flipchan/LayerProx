#!/usr/bin/env python
# coding: utf-8
#socks5 server by Filip Kalebo(flipchan) , support both tcp and udp so that you can proxy torrents and simular 


#->
import sys
import argparse
from socks1 import *    #import all the socks from the file 
from twisted.internet import reactor
#from twisted.protocols import socks
from twisted.python import log


sys.path.append('.')

import marionette_tg.conf


def startthestuff(port, address):
    ip = address
    s5 = Socks5(address, port)
    s5.start()
    return 'started socks5 on ' + str(address) + ' with port ' + str(port) #outputs? atm no..
    
parser = argparse.ArgumentParser(
    description='SOCKS5 proxy server.')
parser.add_argument('--local_port', '-lport', dest='local_port', required=True,
    help='local port to listen on for HTTP requests')
args = parser.parse_args()

SOCKS_PORT = int(args.local_port)
port = SOCKS_PORT
address = '0.0.0.0'

if '__main__' == __name__:
    if marionette_tg.conf.get("general.debug"):
        log.startLogging(sys.stdout)

    #reactor.listenTCP(SOCKS_PORT, socks.SOCKSv4Factory(None))   
    startthestuff(port, address)
    reactor.run()



#<---
