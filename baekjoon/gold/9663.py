import sys
import math


## 기본적인 백트래킹 알고리즘.
line1 = sys.stdin.readline().strip()
N = int(line1)

def sol_queen(N):
    sol_nums=0
    TABLE = [ None for _ in range(N)] ## 0~N-1번째 기물의 y좌표. x좌표는 각 기물의 순서와 같다.
    def conflict(num,y): ## num: 새로놓는 기물이 몇번째 기물인지 y: 새로놓는 기물의 y좌표
        for i in range(num):
            native_x = i
            native_y = TABLE[i]
            immigrant_x = num
            immigrant_y = y
            if abs(immigrant_x-native_x) == abs(immigrant_y-native_y) or native_y == immigrant_y:
                return True
            else:
                continue
        return 0

    def n_queen(n): ## n: 몇번째 기물인지(0부터 시작)
        nonlocal sol_nums
        if n<1:
            for i in range(N):
                TABLE[n] = i
                n_queen(n+1)
                TABLE[n] = None
        else:
            if n==N:
                sol_nums+=1
                return
            for y in range(N): ## y: 새로놓을 기물의 y좌표
                if not conflict(n,y): ## 새로놓을 기물과 이전에 놓은 기물들이 서로 공격가능한지 확인.
                    TABLE[n] = y
                    n_queen(n+1)
                    TABLE[n] = None
                
    n_queen(0)
    
    print(sol_nums)

sol_queen(N)



# def solve_n_queens_improved(N):
#     def is_not_under_attack(row, col):
#         for prev_row in range(row):
#             if board[prev_row] == col or \
#                (prev_row - row) == (board[prev_row] - col) or \
#                (prev_row - row) == (col - board[prev_row]):
#                 return False
#         return True

#     def place_queen(n, row):
#         if row == N:
#             nonlocal solutions
#             solutions += 1
#             return
#         for col in range(N):
#             if is_not_under_attack(row, col):
#                 board[row] = col
#                 place_queen(n, row + 1)
#                 board[row] = -1

#     solutions = 0
#     board = [-1] * N
#     place_queen(N, 0)
#     return solutions

# # Calculate the number of solutions for N=4 using the improved algorithm
# n_queens_solutions_improved = solve_n_queens_improved(8)
# print(n_queens_solutions_improved)


# line1 = sys.stdin.readline().strip()
# N = int(line1)

# def n_queens (i, col):
#     n = len(col) -1
#     if (promising(i, col)):
#         if (i == n):
#             print(col[1: n+1])
#         else:
#             for j in range(1, n+1):
#                 col[i+1] = j
#                 n_queens(i+1, col)

# def promising (i, col):
#     k = 1
#     flag = True
#     while (k < i and flag):
#         if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
#             flag = False
#         k += 1
#     return flag



#### 테스트 통과 알고리즘
line1 = sys.stdin.readline().strip()
N = int(line1)

def solveNQueens(N):
    solutions = 0
    # Bit vectors for columns, diagonals, and anti-diagonals
    columns = 0
    diagonals = 0
    antiDiagonals = 0

    def solve(row, columns, diagonals, antiDiagonals):
        nonlocal solutions
        if row == N:
            solutions += 1
            return
        # Generate possible positions
        possible_positions = (~(columns | diagonals | antiDiagonals)) & ((1 << N) - 1)
        while possible_positions:
            # Choose the rightmost available positionz
            position = possible_positions & -possible_positions
            # Remove chosen position from possible positions
            possible_positions -= position
            solve(row + 1, columns | position, (diagonals | position) << 1, (antiDiagonals | position) >> 1)

    solve(0, columns, diagonals, antiDiagonals)
    return solutions
print(solveNQueens(N))