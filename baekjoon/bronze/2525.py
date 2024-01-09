import sys
line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()
ABinput_list = line1.split()
Cinput = int(line2)
hour = int(ABinput_list[0])
min = int(ABinput_list[1])
total_min = hour*60 + min + Cinput
hour = (total_min//60)%24
min = total_min%60
print(f"{hour} {min}")