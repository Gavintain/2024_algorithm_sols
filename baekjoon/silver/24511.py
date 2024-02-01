import sys
import math
from collections import deque

line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()
line3 = sys.stdin.readline().strip()
line4 = sys.stdin.readline().strip()
line5 = sys.stdin.readline().strip()
N = int(line1)
A=line2.split()
B=line3.split()
M=int(line4)
C=line5.split()

qs=deque()
for i in range(N):
    if int(A[i]):
        pass
    else:
        qs.append(B[i])

for ele in C:
    qs.appendleft(ele)
    print(qs.pop(),end=' ')


