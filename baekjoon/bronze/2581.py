import sys
import math
line1= sys.stdin.readline().strip()
line2= sys.stdin.readline().strip()
M=int(line1)
N=int(line2)
def isprime(N):
    n=math.sqrt(N)
    if N==1:
        return False
    elif n<2:
        return True
    else:
        n=math.ceil(n)
        for i in range(2,n+1):
            if N%i==0:
                return False
            else:
                continue
        else:
            return True
    
SUM=0
MIN=10000

for i in range(M,N+1):
    if isprime(i):
        if i<MIN:
            MIN=i
        SUM+=i
    else:
        continue

if SUM==0:
    print(-1)
else:
    print(f"{SUM}\n{MIN}")

### O(sqrt(n))에 해결가능하다..
### 소수의 제곱수인 경우가 가장 적은 원소로 이루어진 비소수이다.
### 따라서 n의 제곱근에 해당하는 수까지만 나누어 떨어지는지 확인하면 된다.