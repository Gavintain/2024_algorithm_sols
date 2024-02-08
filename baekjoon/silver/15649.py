import sys
from itertools import permutations

line1 = sys.stdin.readline().strip()
lst = line1.split()
N = int(lst[0])
M = int(lst[1])
num_list = [i for i in range(1,N+1)]
ret_list = []
for com in permutations(num_list,M):
    s = ''
    for num in com:
        s += str(num) + ' '
    ret_list.append(s)
ret_list.sort()
for seq in ret_list:
    print(seq)
        