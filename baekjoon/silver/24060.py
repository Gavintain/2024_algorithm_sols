import sys
import statistics

line1 = sys.stdin.readline().strip()
lst = line1.split()
N=int(lst[0])
K=int(lst[1])
ret = []
line2 = sys.stdin.readline().strip()
array = list(map(int, line2.split())) 

def merge(arr,p,q,r):
    i,j,k = p,r+1,p
    tmp_lst = []
    while(i<=r and j<=q):
        if arr[i]>arr[j]:
            tmp_lst.append(arr[j])
            ret.append(arr[j])
            j+=1
        else:
            tmp_lst.append(arr[i])
            ret.append(arr[i])
            i+=1
    while(i<=r):
        tmp_lst.append(arr[i])
        ret.append(arr[i])
        i+=1
    while(j<=q):
        tmp_lst.append(arr[j])
        ret.append(arr[j])
        j+=1
    while(k<=q):
        arr[k] = tmp_lst[k-p]
        k+=1

def merge_sort(arr,p,q):
    if p!=q:
        r = (p+q)//2
        merge_sort(arr,p,r)
        merge_sort(arr,r+1,q)
        merge(arr,p,q,r)

merge_sort(array,0,N-1)
print(-1) if K>len(ret) else print(ret[K-1])
