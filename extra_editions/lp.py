import os, sys
import argparse


parser = argparse.ArgumentParser(description='LayerProx Obfusicated encryption Proxy')

parser.add_argument('--socks5', help='Listen with a socks5')
parser.add_argument('--socks4a', help='Listen with a socks4a')
parser.add_argument('--port', help='define port')
parser.add_argument('--host', help='host address to listen on')
parser.add_argument('--format', help='choice a format')
parser.add_argument('--webui', help='enable webui on port 80')
parser.add_argument('--daemon', help='run as daemon with systemd')
parser.add_argument('--server-mode', help='run as server')
parser.add_argument('--client-mode', help='run as client')
args = parser.parse_args()

print 'useage: layerprox --help'
