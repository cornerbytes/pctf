#!/usr/bin/env python3
from z3 import Ints, Solver, sat
import socket

HOST = "localhost"
PORT = 7489

data = b''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    status = 1
    while status:
        if d:=s.recv(0x1024):
            data+=d
        else:
            status = 0

data = data.split(b"\n")

n = int(data[0][len("n="):].decode())
e = int(data[1][len("e="):].decode())
c = int(data[2][len("c="):].decode())
paq = int(data[3][len("p+q="):].decode())

p,q = Ints("p q")
solver = Solver()
solver.add(p*q == n)
solver.add(p+q == paq)
if solver.check() == sat:
    p = solver.model()[p].as_long()
    q = solver.model()[q].as_long()

#from sympy import symbols, solve, Eq
#p,q = symbols("p q")
#equations = [Eq(p*q, n), Eq(p+q, paq)]
#solutions = solve(equations, p, q)
#p = int(solutions[0][0])
#q = int(solutions[0][1])

try:
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    flag = bytes.fromhex(hex(pow(c,d,n))[2:])
    print(flag)
except Exception as e:
    print(f"haiyya {e}")

