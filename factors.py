#!/usr/bin/python3

import sys
import subprocess

def check_factor(*args):
    if len(args) != 3:
        i = 0
        q = 1
        for a in args:
            if i > 1:
                q *= a
            i += 1
    else:
        q = args[2]
    
    p = args[1]
    num = str(args[0]).replace(':', '=')

    factors = 1 if q > p else 0
    if factors == 1:
        numcp = p
        p = q
        q = numcp
    
    print(num + str(p) + "*" + str(q))

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)
else:
    with open(sys.argv[1], 'r') as f:
        for line in f:
            factors = subprocess.check_output(["factor", line.strip()])
            check_factor(*list(map(int, factors.decode().split()[1:])))
