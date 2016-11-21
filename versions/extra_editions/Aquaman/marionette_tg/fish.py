from os import urandom
import base64

#
#LayerProx aquaman edition
#
#python
#>>> from fish import generatefish
#>>> test = generatefish()
#>>> print test
#fish_GzLCTPDKlNY5n+o2x4NF


def generatefish():
    fish = 'fish_' + base64.b64encode(urandom(15))
    return fish

