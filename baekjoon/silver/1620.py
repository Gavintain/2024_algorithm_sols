import sys

line1= sys.stdin.readline().strip()
NM=line1.split()
N=int(NM[0])
M=int(NM[1])
name_dict={}
num_dict={}

i=0
while(i<N):
    i+=1
    line2= sys.stdin.readline().strip()
    name_dict[str(i)] = line2
    num_dict[line2] = str(i)

i=0
while(i<M):
    i+=1
    line2= sys.stdin.readline().strip()
    if line2 in name_dict.keys():
        print(name_dict[line2])
    else:
        print(num_dict[line2])