import sys

## 테뷸레이션을 위한 테이블
table = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]
## 사실상 재귀호출 전에 미리 알 수 있는 테이블 값들을 채우기
for i in range(21):
    for j in range(21):
        table[i][j][0] = 1
        table[i][0][j] = 1
        table[0][i][j] = 1
## 리스트 원소를 정수로 변환하기 위한 유틸함수
def ToInt(x):
    return int(x)

def f(a,b,c):
    if (a<=0)or(b<=0)or(c<=0):
        return 1
    elif (a>20)or(b>20)or(c>20):
        ret = f(20,20,20) if table[20][20][20] == None else table[20][20][20]
        table[20][20][20] = ret
        return ret
    elif (a<b)and(b<c):
        ret=0
        ret += f(a,b,c-1) if table[a][b][c-1] == None else table[a][b][c-1]
        ret += f(a,b-1,c-1) if table[a][b-1][c-1] == None else table[a][b-1][c-1]
        ret -= f(a,b-1,c) if table[a][b-1][c] == None else table[a][b-1][c]
        table[a][b][c] = ret
        return ret
    else:
        ret=0
        ret += f(a-1,b,c) if table[a-1][b][c] == None else table[a-1][b][c]
        ret += f(a-1,b-1,c) if table[a-1][b-1][c] == None else table[a-1][b-1][c]
        ret += f(a-1,b,c-1) if table[a-1][b][c-1] == None else table[a-1][b][c-1]
        ret -= f(a-1,b-1,c-1) if table[a-1][b-1][c-1] == None else table[a-1][b-1][c-1]
        table[a][b][c] = ret
        return ret

while(True):
    line1= sys.stdin.readline().strip()
    lst = list(map(int,line1.split()))
    if (lst[0]==-1)and(lst[1]==-1)and(lst[2]==-1):
        break
    else:
        print(f"w({lst[0]}, {lst[1]}, {lst[2]}) = {f(lst[0],lst[1],lst[2])}")