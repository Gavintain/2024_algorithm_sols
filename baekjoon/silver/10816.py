import sys
from collections import defaultdict

line1= sys.stdin.readline().strip()
line2= sys.stdin.readline().strip()
line3= sys.stdin.readline().strip()
line4= sys.stdin.readline().strip()

N=int(line1)
num_list = line2.split()
M = int(line3)
task_list = line4.split()
num_dict=defaultdict(int)

i=0
while(i<N):
    num_dict[num_list[i]]+=1
    i+=1

i=0
for task in task_list:
    print(num_dict[task],end=' ')
