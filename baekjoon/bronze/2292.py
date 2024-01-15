import sys
import math
## an = 1+3n(n-1)
line = sys.stdin.readline().strip()
N = int(line)
if N==1:
    print(1)
else:
    z = (N-1)/3
    Z = math.sqrt(1+4*z)/2
    Z = Z//1
    while(1+3*Z*(Z-1) < N):
        Z+=1
    print(int(Z))

