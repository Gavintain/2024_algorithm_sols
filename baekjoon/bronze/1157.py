import sys
ABC_dict = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,
            'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,
            'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
max = 0
ret='A'
max = ABC_dict['A']
line = sys.stdin.readline().strip()
for alphabat in line:
    ABC_dict[alphabat.upper()]+=1
for key in ABC_dict.keys():
    if ABC_dict[key]>max:
        max = ABC_dict[key]
        ret = key
    elif ABC_dict[key]==max:
        ret = '?'
    else:
        pass
print(ret)