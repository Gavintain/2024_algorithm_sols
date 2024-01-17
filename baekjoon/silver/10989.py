import sys

line1= sys.stdin.readline().strip()
N=int(line1)

lst=[0 for _ in range(10000)]

for _ in range(N):
    line2= sys.stdin.readline().strip()
    n=int(line2)
    lst[n-1]+=1

i=0
for count in lst:
    i+=1
    for _ in range(count):
        print(i)


