from bintrees import has_fast_tree_support
from pwn import *

def getNewAVL(seq):
	if has_fast_tree_support():
		from bintrees import FastAVLTree
		return FastAVLTree(seq)
	else:
		from bintrees import AVLTree
		return AVLTree(seq)

conn = remote('misc.chal.csaw.io', 9001)
conn.recvline() # Skip line telling us how to do it
sequence = [(int(val.strip()), int(val.strip())) for val in conn.recvline().split(',')]
conn.recvline() # Skip line telling us how to do it

tree = getNewAVL(sequence)
preorder = []
# -1 means preorder
tree.foreach(lambda k,v: preorder.append(str(v)), -1)

print("Preorder: %s" % repr(preorder))
preorder = ','.join(preorder)
print("Final preorder: %s" % preorder)
conn.sendline(preorder)
conn.interactive()
