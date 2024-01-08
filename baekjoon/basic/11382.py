import sys
line = sys.stdin.readline().strip()
ABC_list = line.split()
A,B,C = int(ABC_list[0]),int(ABC_list[1]),int(ABC_list[2])
print(A+B+C)
