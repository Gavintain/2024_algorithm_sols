# import sys
# import math

# def f(number):
#     if number <2:
#         return False
#     elif number == 2:
#         return True
#     else: 
#         m = math.ceil(math.sqrt(number))
#         i=2
#         while(i<=m):
#             if number%i==0:
#                 return False
#             i+=1
#         return True

# line1 = sys.stdin.readline().strip()
# n = int(line1)
# table = {}

# for _ in range(n):
#     line2 = sys.stdin.readline().strip()
#     num = int(line2)
#     p_count=0
#     for i in range(2,num//2+1):
#         if i not in table.keys():
#             table[i] = f(i)
#         if table[i]:
#             if num - i not in table.keys():
#                 table[num - i] = f(num - i)
#             if table[num - i]:
#                 p_count+=1
#     print(p_count)

import sys
import math

def f(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    
    m = math.ceil(math.sqrt(number))
    for i in range(3, m + 1, 2):
        if number % i == 0:
            return False
    return True

line1 = sys.stdin.readline().strip()
n = int(line1)

table = {}

for _ in range(n):
    line2 = sys.stdin.readline().strip()
    num = int(line2)
    p_count=0
    for i in range(2,num//2+1):
        if i not in table.keys():
            table[i] = f(i)
        if table[i]:
            if num - i not in table.keys():
                table[num - i] = f(num - i)
            if table[num - i]:
                p_count+=1
    print(p_count)