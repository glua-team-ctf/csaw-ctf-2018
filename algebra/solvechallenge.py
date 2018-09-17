from pwn import *
from sympy import sympify, solve, Symbol

def solveStrEq(strEq):
	X = Symbol('X')
	sympyEq = sympify('Eq(%s)' % strEq.replace('=', ','))
	return solve(sympyEq)[0]

conn = remote('misc.chal.csaw.io', 9002)
conn.recvline_endswith('*')

while True:
	try:
		equation = conn.recvline(keepends=False)
		print("Solving %s..." % equation)
		print("p.s.: simpy converted eq: %s" % ('Eq(%s)' % equation.replace('=', ',')))
		solution = float(solveStrEq(equation))
		print("\tSolved: %s" % solution)
		print(conn.recvuntil('What does X equal?: ') + str(solution))
		conn.sendline(str(solution))
		line = conn.recvline(keepends=False)
		print(line)
		if line != "YAAAAAY keep going":
			print("Solution was wrong.")
			print("Received: %s" % line)
			print("Rest of stream: %s" & conn.recv())
			break
	except:
		the_type, the_value, the_traceback = sys.exc_info()
		if the_type == EOFError:
			print("Hit EOF?")
			print(conn.recv())
		print("Failed to parse/solve equation (probably): %s" % str(the_value))
		print("#yolo gonna answer 0.")
		conn.recvuntil('What does X equal?: ')
		conn.sendline('0')
		line = conn.recvline(keepends=False)
		if line != "YAAAAAY keep going":
			print("Solution was wrong.")
			print("Received: %s" % line)
			print("Rest of stream: %s" & conn.recv())
