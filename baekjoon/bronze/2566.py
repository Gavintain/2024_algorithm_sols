import sys
X=1
Y=1
MAX=-1

line = sys.stdin.readline().strip()
row=1
while(line!=''):
    lst = line.split()
    col=1

    for element in lst:
        if int(element)>MAX:
            X=col
            Y=row
            MAX = int(element)
        col+=1

    row+=1
    line = sys.stdin.readline().strip()

print(f'{MAX}\n{Y} {X}')

