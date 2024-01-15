import sys
MAJORGPA = 0
CREDITS = 0
GPA_dict = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}

line = sys.stdin.readline().strip()
while(line!=''):
    object_credits_gpa = line.split()

    if object_credits_gpa[2] =='P':
        pass
    else:
        CREDITS+=float(object_credits_gpa[1])
        MAJORGPA+=float(object_credits_gpa[1])*GPA_dict[object_credits_gpa[2]]

    line = sys.stdin.readline().strip()

print(MAJORGPA/CREDITS)
