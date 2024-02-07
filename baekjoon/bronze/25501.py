import sys
import math


def IsPal(string,i,j,num_call):
    num_call+=1
    if i==j:
        return 1,num_call
    elif i>j:
        return 1,num_call
    elif string[i]!=string[j]:
        return 0,num_call
    else:
        return IsPal(string,i+1,j-1,num_call)


line1 = sys.stdin.readline().strip()
n = int(line1)

i=0
while(i<n):
    line2 = sys.stdin.readline().strip()
    ret = IsPal(line2,0,len(line2)-1,0)
    print(f"{ret[0]} {ret[1]}")
    i+=1
