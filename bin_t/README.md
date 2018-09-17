# bin_t
## Misc
Binary trees let you do some interesting things. Can you balance a tree?

`nc misc.chal.csaw.io 9001`

Equal nodes should be inserted to the right of the parent node. You should balance the tree as you add nodes.

## Solution
The challenge simply asked you to insert all numbers it gave you into an AVL then send the preorder of the built tree in the end.

Packages: `bintrees` and `pwntools` (for its `remote` function).

Code: [solvechallenge.py](./solvechallenge.py)
