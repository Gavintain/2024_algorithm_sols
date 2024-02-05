import sys
import statistics

def kantor(string,p,q):
    if p!=q:
        l = q - p + 1
        r1 = p + l//3
        r2 = p + l//3 + l//3
        i = r1
        kantor(string,p,r1-1)
        kantor(string,r2,q)
        while(i<=r2-1):
            string[i] = ' '
            i+=1


line1 = sys.stdin.readline().strip()
while(line1 !=''):
    N = 3**int(line1)
    s = ['-' for _ in range(N)]
    kantor(s,0,N-1)
    print(''.join(s))
    line1 = sys.stdin.readline().strip()

