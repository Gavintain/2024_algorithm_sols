import sys
import math

line1 = sys.stdin.readline().strip()
n = int(line1)

def test(n):
    number_call_dynamic = 0
    def Naive_fibo(n):
        if n ==1 or n == 2 :
            return 1 
        else :
            return Naive_fibo(n-1)+Naive_fibo(n-2)
    ## 메모이제이션
    # def Dynamic_fibo(n):
    #     table = [None for _ in range(n+1)]
    #     table[1] = 1
    #     table[2] = 1
    #     def Dynamic_start(n):
    #         nonlocal number_call_dynamic
    #         number_call_dynamic+=1
    #         if table[n]!=None :
    #             return table[n] 
    #         else:
                    # table[n] = Dynamic_start(n-1) + Dynamic_start(n-2)
                    # return table[n]
    #     Dynamic_start(n)

    ## 테뷸레이션    
    def Dynamic_fibo(n):
        table = [None for _ in range(n+1)]
        table[1] = 1
        table[2] = 1
        for i in range(3,n+1):
            table[i] = table[i-1] + table[i-2]
            nonlocal number_call_dynamic
            number_call_dynamic+=1
        return table[n]
    number_call_naive = Dynamic_fibo(n)
    print(f'{number_call_naive} {number_call_dynamic}')

test(n)