import sys
import math
line1 = sys.stdin.readline()
line2 = sys.stdin.readline()
n = int(line1)
lst = line2.split()
n0=1
stack=[]

i=0
while(n0<n+1):
    if len(stack)<1:
        current_man = int(lst[i])
        if current_man == n0:
            n0+=1
            i+=1
        else:
            stack.append(current_man)
            i+=1
    else:   
        wait_man = stack.pop()
        if wait_man == n0:
            n0+=1
            continue
        else:
            current_man = int(lst[i])
            if current_man == n0:
                n0+=1
                i+=1
                stack.append(wait_man)
            else:
                if current_man>wait_man:
                    break
                else:
                    stack.append(wait_man)
                    stack.append(current_man)
                    i+=1
    print(stack,n0,i)
if n0>n:
    print("Nice")
else:
    print("Sad")