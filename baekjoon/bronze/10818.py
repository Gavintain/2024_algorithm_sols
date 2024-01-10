import sys
line1= sys.stdin.readline().strip()
line2= sys.stdin.readline().strip()
N = int(line1)
numlst = [int(x) for x in line2.split()]
n_max = numlst[0]
n_min = numlst[0]
for num in numlst:
    if num > n_max:
        n_max = num
    elif num < n_min:
        n_min = num
    else:
        pass
print(f'{n_min} {n_max}')
    
