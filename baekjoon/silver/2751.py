# import sys

# def f_sorting(lst,number,l):
#     if l<3:
#         lst.append(number)
#         lst.sort()
#         return lst
#     else:
#         if l%2==0:
#             mid = lst[l//2]
#             if number>mid:
#                 return lst[:l//2]+[mid]+ f_sorting(lst[l//2+1:],number,l//2-1)
#             else:
#                 return f_sorting(lst[:l//2],number,l//2) + [mid] + lst[l//2+1:]
#         else:
#             mid = lst[l//2]
#             if number>mid:
#                 return lst[:l//2]+[mid]+ f_sorting(lst[l//2+1:],number,l//2)
#             else:
#                 return f_sorting(lst[:l//2],number,l//2) + [mid] + lst[l//2+1:]

# line1= sys.stdin.readline().strip()
# N=int(line1)

# lst=[]
# L=0
# for _ in range(N):
#     line2= sys.stdin.readline().strip()
#     n=int(line2)
#     if L==0:
#         lst.append(n)
#         L+=1
#     else:
#         lst = f_sorting(lst,n,L)
#         L+=1


# for num in lst:
#     print(num)
    
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
#########################


# import sys

# def f_sorting(lst, start, end):
#     l = end - start + 1
#     if l < 5:
#         lst[start:end+1] = sorted(lst[start:end+1])
#         return
#     else:

#         section_length = l // 5
#         tmp_lst = [max(lst[start:start+section_length]), max(lst[start+section_length:start+2*section_length]), max(lst[start+2*section_length:start+3*section_length]), max(lst[start+3*section_length:start+4*section_length]), max(lst[start+4*section_length:end+1])]
#         tmp_lst.sort()
#         mid = tmp_lst[2]

        
#         left = start
#         right = end
#         while left <= right:
#             while left <= right and lst[left] < mid:
#                 left += 1
#             while left <= right and lst[right] >= mid:
#                 right -= 1
#             if left <= right:
#                 lst[left], lst[right] = lst[right], lst[left]
#                 left += 1
#                 right -= 1
        

#         if start < right:
#             f_sorting(lst, start, right)
#         if left < end:
#             f_sorting(lst, left, end)


# line1= sys.stdin.readline().strip()
# N=int(line1)

# lst=[]
# L=0
# for _ in range(N):
#     line2= sys.stdin.readline().strip()
#     n=int(line2)
#     lst.append(n)

# f_sorting(lst, 0, len(lst) - 1)
# for num in lst:
#     print(num)

