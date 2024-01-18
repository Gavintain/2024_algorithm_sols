# import sys

# line1= sys.stdin.readline().strip()
# N=int(line1)

# lst=[]
# L=0
# for _ in range(N):
#     line2= sys.stdin.readline().strip()
#     n=int(line2)
#     lst.append(n)

# lst.sort()
# for num in lst:
#     print(num)
########################


#### 노움정렬
# import sys

# line1= sys.stdin.readline().strip()
# N=int(line1)

# lst=[]
# L=0
# for _ in range(N):
#     line2= sys.stdin.readline().strip()
#     n=int(line2)
#     lst.append(n)

# j=1
# while(j<N):
#     if lst[j-1]>lst[j]:
#         old = lst[j-1]
#         lst[j-1] = lst[j]
#         lst[j] = old
#         if j==1:
#             j+=1
#         else:
#             j-=1
#     else:
#         j+=1

# for num in lst:
#     print(num) 


# ####### 삽입정렬
# import sys

# line1= sys.stdin.readline().strip()
# N=int(line1)

# lst=[]
# L=0
# for _ in range(N):
#     line2= sys.stdin.readline().strip()
#     n=int(line2)
#     lst.append(n)

# for i in range(1,N):
#     j=i-1
#     key = lst[i]
#     while(lst[j]>key and j>=0):
#         lst[j+1] = lst[j]
#         j-=1
#     lst[j+1] = key

# for num in lst:
#     print(num) 


# #### 버블정렬
# import sys

# line1= sys.stdin.readline().strip()
# N=int(line1)

# lst=[]
# L=0
# for _ in range(N):
#     line2= sys.stdin.readline().strip()
#     n=int(line2)
#     lst.append(n)

# for i in range(N):
#     j=N-1
#     while(j>=i):
#         if lst[j]<lst[j-1]:
#             old = lst[j-1]
#             lst[j-1] = lst[j]
#             lst[j] = old
#         j-=1


# for num in lst:
#     print(num) 


#### 퀵정렬(단순피벗선택,인플레이스 정렬, 재귀대신 반복문형태)
# import sys

# line1= sys.stdin.readline().strip()
# N=int(line1)

# lst=[]
# L=0
# for _ in range(N):
#     line2= sys.stdin.readline().strip()
#     n=int(line2)
#     lst.append(n)

# loop_stack = [(0,N-1)]

# while(len(loop_stack)>0):
#     start,end = loop_stack.pop()
#     pivot = lst[end]
#     idx_pivot = start-1
#     cursor=start
#     while(cursor<=end):
#         if lst[cursor]<=pivot:
#             idx_pivot+=1
#             old = lst[idx_pivot]
#             lst[idx_pivot] = lst[cursor]
#             lst[cursor] = old
#         cursor+=1
#     if idx_pivot-start>=2:
#         loop_stack.append((start,idx_pivot-1))
#     if end-idx_pivot>=2:
#         loop_stack.append((idx_pivot+1,end))

# for num in lst:
#     print(num) 



###### GPT 완전 인플레이스 정렬과 반복문 형태의 퀵정렬.
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def iterative_quick_sort(arr):
    low = 0
    high = len(arr) - 1
    size = high - low + 1
    stack = [0] * size
    top = -1
    top += 1
    stack[top] = low
    top += 1
    stack[top] = high
    while top >= 0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1
        p = partition(arr, low, high)
        if p-1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = p - 1
        if p+1 < high:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = high

import sys

line1= sys.stdin.readline().strip()
N=int(line1)
lst=[]
L=0
for _ in range(N):
    line2= sys.stdin.readline().strip()
    n=int(line2)
    lst.append(n)

iterative_quick_sort(lst)
for num in lst:
    print(num) 