import sys
import statistics

line1 = sys.stdin.readline().strip()
n = int(line1)

i=0
lst = []
while(i<n):
    line2 = sys.stdin.readline().strip()
    num = int(line2)
    lst.append(num)
    i+=1
m = sorted(statistics.multimode(lst))
print(m)
if len(m)>1:
    print(f'{int(round(statistics.mean(lst),0))}\n{statistics.median(lst)}\n{m[1]}\n{max(lst)-min(lst)}')
else:
    print(f'{int(round(statistics.mean(lst),0))}\n{statistics.median(lst)}\n{m[0]}\n{max(lst)-min(lst)}')