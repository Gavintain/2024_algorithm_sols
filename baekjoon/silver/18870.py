import sys
line1= sys.stdin.readline().strip()
N = int(line1)
line2= sys.stdin.readline().strip()
lst = line2.split()
lst = [int(x) for x in lst]
# unique_lst = list(dict.fromkeys(lst))
unique_lst = list(set(lst))
unique_lst.sort()
dct = {unique_lst[i]:i for i in range(len(unique_lst))}

print(' '.join(str(dct[x]) for x in lst))
##########
# import sys
# line1= sys.stdin.readline().strip()
# N = int(line1)
# line2= sys.stdin.readline().strip()
# lst = line2.split()
# new_lst = [int(i) for i in lst]

# indexed_lst = list(enumerate(new_lst))
# indexed_lst.sort(key=lambda x: x[1])

# # 각 숫자가 처음 나타나는 인덱스를 저장할 사전
# first_occurrence = {}
# score_lst = [0] * N

# for i, (original_index, value) in enumerate(indexed_lst):
#     # 숫자가 처음 나타나는 위치를 기록
#     if value not in first_occurrence:
#         first_occurrence[value] = i

# for original_index, value in indexed_lst:
#     # 각 숫자보다 작은 숫자의 개수는 그 숫자가 처음 나타나는 인덱스와 같다
#     score_lst[original_index] = first_occurrence[value]

# print(' '.join(str(x) for x in score_lst))

# import sys
# line1= sys.stdin.readline().strip()
# N = int(line1)
# line2= sys.stdin.readline().strip()
# lst = line2.split()
# lst = [int(x) for x in lst]
# unique_lst = list(dict.fromkeys(lst))
# dct = {x:0 for x in unique_lst}

# for i in range(len(unique_lst)-1):
#     for j in range(i,len(unique_lst)):
#         if unique_lst[i]>unique_lst[j]:
#             dct[unique_lst[i]]+=1
#         elif unique_lst[i]<unique_lst[j]:
#             dct[unique_lst[j]]+=1

# print(' '.join(str(dct[x]) for x in lst))