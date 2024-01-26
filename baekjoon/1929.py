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
nm = line1.split()
n = int(nm[0])
m = int(nm[1])

for num in range(n,m+1):
    if f(num):
        print(num)
    
