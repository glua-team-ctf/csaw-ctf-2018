#!/usr/bin/env python2

from IPython import embed
from pwn import *

#prod_tube = remote('reversing.chal.csaw.io', 9000)

client_tube = remote('reversing.chal.csaw.io', 9002)
client_tube.send('\n')
cdata = client_tube.recvall()
print('cdata', cdata)

dev_tube = remote('reversing.chal.csaw.io', 9001)
dev_tube.send(cdata)
ddata = dev_tube.recvall()
print('ddata', ddata)

embed()

client_tube.close()
dev_tube.close()
#prod_tube.close()
