import sys
import math

line1 = sys.stdin.readline().strip()
N = int(line1)

def sol_queen(N):
    sol_nums=0
    TABLE = [[0 for _ in range(N)] for _ in range(N)]
    def conflict(location1,location2):
        if location1[0] == location2[0] or location1[1] == location2[1]:
            return 1
        elif abs(location2[0]-location1[0]) == abs(location2[1]-location1[1]):
            return 1
        else:
            return 0

    def n_queen(previous_row,n):
        if n<1:
            nonlocal sol_nums
            sol_nums+=1
        else:
            for col in range(N):
                if TABLE[previous_row][col]
            pass
            
    for row in range(N):
        n_queen(row,N)
    
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

