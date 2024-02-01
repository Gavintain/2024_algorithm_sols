# import sys
# import math

# def factorial(N):
#     ret=1
#     for i in range(1,N+1):
#         ret*=i
#     return ret

# line1 = sys.stdin.readline().strip()
# T=int(line1)
# i=0
# while(i<T):
#     line2 = sys.stdin.readline().strip()
#     lst = line2.split()
#     N=int(lst[0])
#     M=int(lst[1])
#     print(int(factorial(M)/(factorial(M-N)*factorial(N))))
#     i+=1

import sys
import math

line1 = sys.stdin.readline().strip()
T=int(line1)
i=0
while(i<T):
    line2 = sys.stdin.readline().strip()
    lst = line2.split()
    N=int(lst[0])
    M=int(lst[1])
    print(math.comb(M,N))
    i+=1




