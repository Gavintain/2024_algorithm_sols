import sys
import math

def f(number):
    if number <2:
        return False
    elif number == 2:
        return True
    else: 
        m = math.ceil(math.sqrt(number))
        i=2
        while(i<=m):
            if number%i==0:
                return False
            i+=1
        return True

line1= sys.stdin.readline().strip()
n = int(line1)

i=0
while(i<n):
    i+=1
    line2 = sys.stdin.readline().strip()
    num = int(line2)
    while(True):
        if f(num):
            print(num)
            break
        else:
            num+=1
    
