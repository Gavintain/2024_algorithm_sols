# import sys
# from itertools import permutations

# line1 = sys.stdin.readline().strip()
# N = int(line1)
# line2 = sys.stdin.readline().strip()
# num_list = list(map(int,line2.split()))
# line3 = sys.stdin.readline().strip()

# oper_count_list  = list(map(int,line3.split()))
# oper_list = ['+']*oper_count_list[0] + ['-']*oper_count_list[1] + ['*']*oper_count_list[2] + ['/']*oper_count_list[3]

# eq_list = []

# for permut in permutations(oper_list,N-1):
#     if permut in eq_list:
#         pass
#     else:
#         eq_list.append(permut)

# MAX = -1000000001
# MIN = 1000000001
# for eq in eq_list:
#     i=0
#     ret = num_list[0]
#     for operator in eq:
#         if operator == '+':
#             ret += num_list[i+1]
#         elif operator == '-':
#             ret -= num_list[i+1]
#         elif operator == '*':
#             ret *= num_list[i+1]
#         else:
#             if ret<0 and num_list[i+1]>0:
#                 ret = -(ret)
#                 ret //= num_list[i]
#                 ret = -(ret)
#             else:
#                 ret //= num_list[i+1]
#         i+=1
#     if ret < MIN:
#         MIN = ret
#     if ret > MAX:
#         MAX = ret
# print(f'{MAX}\n{MIN}')

import sys
from itertools import permutations

line1 = sys.stdin.readline().strip()
N = int(line1)
line2 = sys.stdin.readline().strip()
num_list = list(map(int,line2.split()))
line3 = sys.stdin.readline().strip()
oper_count_list  = list(map(int,line3.split()))

MAX = -1000000001
MIN = 1000000001
def custom_cal(maxmin_lst,count_p,count_ma,count_mu,count_d,index,ret):
    if index > N-1:
        maxmin_lst[0] = max(maxmin_lst[0],ret)
        maxmin_lst[1] = min(maxmin_lst[1],ret)
    else:
        if count_p < oper_count_list[0]:
            ret_tmp = ret + num_list[index]
            custom_cal(maxmin_lst,count_p+1,count_ma,count_mu,count_d,index+1,ret_tmp)
        if count_ma < oper_count_list[1]:
            ret_tmp = ret - num_list[index]
            custom_cal(maxmin_lst,count_p,count_ma+1,count_mu,count_d,index+1,ret_tmp)
        if count_mu < oper_count_list[2]:
            ret_tmp = ret * num_list[index]
            custom_cal(maxmin_lst,count_p,count_ma,count_mu+1,count_d,index+1,ret_tmp)
        if count_d < oper_count_list[3]:
            if ret<0 and num_list[index]>0:
                ret_tmp = ret
                ret_tmp = -(ret_tmp)
                ret_tmp //= num_list[index]
                ret_tmp = -(ret_tmp)
            else:
                ret_tmp = ret
                ret_tmp //= num_list[index]
            custom_cal(maxmin_lst,count_p,count_ma,count_mu,count_d+1,index+1,ret_tmp)
maxmin_lst = [MAX,MIN]
ret = num_list[0]
custom_cal(maxmin_lst,0,0,0,0,1,ret)
print(f'{maxmin_lst[0]}\n{maxmin_lst[1]}')