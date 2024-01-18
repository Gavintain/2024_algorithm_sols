import sys

line1 = sys.stdin.readline().strip()
N = int(line1)
line2 = sys.stdin.readline().strip()
lst = line2.split()

line3 = sys.stdin.readline().strip()
M = int(line3)
line4 = sys.stdin.readline().strip()
task = line4.split()

# lst의 원소를 해시맵에 저장합니다.
hash_map = {}
for num in lst:
    hash_map[num] = True

# task의 각 원소가 해시맵(따라서 lst)에 있는지 확인합니다.
for num in task:
    result = 1 if num in hash_map else 0
    print(result, end=' ')