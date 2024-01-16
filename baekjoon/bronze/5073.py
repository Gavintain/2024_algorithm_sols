import sys
import math
line1= sys.stdin.readline().strip()
while(line1!=""):
    if line1=="0 0 0":
        break
    else:
        ABC=line1.split()
        A=int(ABC[0])
        B=int(ABC[1])
        C=int(ABC[2])
        lst = [A,B,C]
        lst.sort()
        if lst[-1]>=lst[0]+lst[1]:
            print("Invalid")
        elif A==B and B==C:
            print("Equilateral")
        elif A==B or A==C or B==C:
            print("Isosceles")
        else:
            print("Scalene")

        line1= sys.stdin.readline().strip()

