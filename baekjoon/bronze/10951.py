import sys
line1 = sys.stdin.readline().strip()
while(line1!=''):
    ABinput_list = line1.split()
    A = int(ABinput_list[0])
    B = int(ABinput_list[1])
    print(A+B)
    line1 = sys.stdin.readline().strip()