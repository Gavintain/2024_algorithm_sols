import sys

line1= sys.stdin.readline().strip()
N=int(line1)
table = {}
i=0
while(i<N):
    line2= sys.stdin.readline().strip()
    name_stat = line2.split()
    if name_stat[1] =='enter':
        table[name_stat[0]] = 1
    else:
        table[name_stat[0]] = 0
    i+=1

ret_lst = []
for key in table.keys():
    if table[key]:
        ret_lst.append(key)

ret_lst.sort(reverse=True)
for ele in ret_lst:
    print(ele)

