import sys
import math
from collections import deque
def f(nx,q):
    command = nx[0]
    if command == 'push':
        x = int(nx[1])
        q.append(x)
    elif command == 'pop':
        print(q.popleft()) if q else print(-1)
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        print(0) if q else print(1)
    elif command == 'front':
        print(q[0]) if q else print(-1)
    else:
        print(q[-1]) if q else print(-1)

line1 = sys.stdin.readline().strip()
n = int(line1)

q = deque()
i=0
while(i<n):
    i+=1
    line2 = sys.stdin.readline().strip()
    nx = line2.split()
    f(nx,q)
