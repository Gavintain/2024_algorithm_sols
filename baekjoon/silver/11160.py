# 문제
# N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

# 예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

# 1	2	3	4
# 2	3	4	5
# 3	4	5	6
# 4	5	6	7
# 여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.

# 표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

# 출력
# 총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.

# 예제 입력 1 
# 4 3
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# 2 2 3 4
# 3 4 3 4
# 1 1 4 4
# 예제 출력 1 
# 27
# 6
# 64
# 예제 입력 2 
# 2 4
# 1 2
# 3 4
# 1 1 1 1
# 1 2 1 2
# 2 1 2 1
# 2 2 2 2
# 예제 출력 2 
# 1
# 2
# 3
# 4
# if __name__ == '__main__':
#     first_line = input()
#     N = first_line.split()

#     M = int(N[1])
#     N = int(N[0])
#     map = [[] for _ in range(N)]

#     tmp = 0
#     for i in range(N):
#         line = input()
#         elements = line.split()
#         for ele in elements:
#             tmp += int(ele)
#             map[i].append(tmp)


#     for i in range(M):
#         line = input()
#         elements = line.split()
#         x1,y1,x2,y2 = int(elements[0]),int(elements[1]),int(elements[2]),int(elements[3])
#         min_x = min(x1,x2)
#         min_y = min(y1,y2)
#         max_x = max(x1,x2)
#         max_y = max(y1,y2)
        
#         ret=int(map[max_y][max_x]) - int(map[min_y][min_x]) 
#         if min_x>0:
#             for j in range(min_y-1,max_y):
#                 ret -= (int(map[][]))
#         print(ret)
import sys


if __name__ == '__main__':
    first_line = sys.stdin.readline().strip()
    N = first_line.split()

    M = int(N[1])
    N = int(N[0])
    map_lst = [[] for _ in range(N)]
    sum_map = [[None]*N for _ in range(N)]
  
    for i in range(N):
        line = sys.stdin.readline().strip()
        elements = line.split()
        for ele in elements:
            map_lst[i].append(int(ele))

    sum_map[0][0] = map_lst[0][0]
    for i in range(N):
        for j in range(N):
            if i<1:
                if j<1:
                    sum_map[i][j] = map_lst[i][j]
                else:
                    sum_map[i][j] = sum_map[i][j-1] + map_lst[i][j]
            else:
                if j<1:
                    sum_map[i][j] = sum_map[i-1][j] + map_lst[i][j]
                else:
                    sum_map[i][j] = sum_map[i-1][j] + sum_map[i][j-1] + map_lst[i][j] - sum_map[i-1][j-1]
    
    for i in range(M):
        line = sys.stdin.readline().strip()
        elements = line.split()
        y1,x1,y2,x2 = int(elements[0]),int(elements[1]),int(elements[2]),int(elements[3])
        ret=0
        if x1<=1:
            if y1<=1:
                ret = sum_map[y2-1][x2-1] 
            else:
                ret = sum_map[y2-1][x2-1] - sum_map[y1-1-1][x2-1]
        else:
            if y1<=1:
                ret = sum_map[y2-1][x2-1] - sum_map[y2-1][x1-1-1]
            else:
                ret = sum_map[y2-1][x2-1] - sum_map[y1-1-1][x2-1] - sum_map[y2-1][x1-1-1] + sum_map[y1-1-1][x1-1-1]
        print(ret)