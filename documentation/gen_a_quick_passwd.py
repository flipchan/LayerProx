from os import urandom
import base64

mynumber = 81 #change this if needed
myl = base64.b64encode(urandom(mynumber))

print 'ur generated key with ' + str(mynumber)  + 'chars is: ' + str(myl)

