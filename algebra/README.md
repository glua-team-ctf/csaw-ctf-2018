# Algebra
## Misc
Are you a real math wiz?

`nc misc.chal.csaw.io 9002`

## Solution
The remote server gives you a bunch of equations to solve which get increasingly bigger and cannot be solved by hand without much effort.

To sove this I used `sympy` and `pwntools` (for its `remote` function).

As some equations came outright wrong (with part of it being `(X - 12) * (18 - 18)`, which nulls out `X` and by doing so invalidates the equation), I made it send `0` as a fallback behavior (which to my surprise worked in most cases).

Code is in [solvechallenge.py](./solvechallenge.py)
