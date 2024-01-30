import sys
import math

def f(nx):
    num = int(nx[0])
    if num == 1:
        x = int(nx[1])
        stack.append(x)
    elif num == 2:
        print(-1) if len(stack)<1 else print(stack.pop())
    elif num == 3:
        print(len(stack))
    elif num == 4:
        print(1) if len(stack)==0 else print(0)
    else:
        print(-1) if len(stack)<1 else print(stack[-1])



line1 = sys.stdin.readline().strip()
n = int(line1)

stack=[]
i=0
while(i<n):
    i+=1
    line2 = sys.stdin.readline().strip()
    nx = line2.split()
    f(nx)
