import sys
import math
line1= sys.stdin.readline().strip()
line2= sys.stdin.readline().strip()
line3= sys.stdin.readline().strip()
n0=int(line3)
c=int(line2)
a1a0=line1.split()
a1=int(a1a0[0])
a0=int(a1a0[1])
if a1*n0+a0>c*n0:
    print(0)
else:
    if a1>c:
        print(0)
    else:
        print(1)
