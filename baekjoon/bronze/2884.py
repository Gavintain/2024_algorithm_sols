# import sys
# line = sys.stdin.readline().strip()
# ABinput_list = line.split()
# A = int(ABinput_list[0])
# B = int(ABinput_list[1])
# hour = A
# min = B-45
# if min<0:
#     hour-=1
#     min += 60
# if hour<0:
#     hour+=24
# print(f"{hour} {min}")

import sys
line = sys.stdin.readline().strip()
ABinput_list = line.split()
hour = int(ABinput_list[0]) + 24
min = int(ABinput_list[1]) + 60
min = min - 45
hour = (hour-1+min//60)%24
min = min%60
print(f"{hour} {min}")