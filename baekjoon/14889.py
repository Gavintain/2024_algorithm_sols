# import sys
# from itertools import combinations

# def divide_2_iter(players):
#     for com1 in combinations(players,len(players)//2):
#         com2 = []
#         for player in players:
#             if player not in com1:
#                 com2.append(player)
#         yield com1,com2

# line1 = sys.stdin.readline().strip()
# n = int(line1)

# i=0
# table = []
# while(i<n):
#     line2 = sys.stdin.readline().strip()
#     table.append(list(map(int,line2.split())))
#     i+=1

# players=[i for i in range(n)]
# min_gap = 100*n
# for team1,team2 in divide_2_iter(players):
#     t1_score,t2_score = 0,0
#     for player1 in team1:
#         for player2 in team1:
#             if player1==player2:
#                 pass
#             else:
#                 t1_score+=table[player1][player2]
#     pre_gap = t1_score
#     for player1 in team2:
#         for player2 in team2:
#             if player1==player2:
#                 pass
#             else:
#                 t2_score+=table[player1][player2]
#                 gap = abs(t1_score-t2_score)
#                 if gap>min_gap:
#                     break
#                 else:
#                     pre_gap = gap

#     if min_gap>abs(t1_score-t2_score):
#         min_gap = abs(t1_score-t2_score)
# print(min_gap)

import sys
from itertools import combinations

def divide_2_iter(players):
    for com1 in combinations(players,len(players)//2):
        com2 = []
        for player in players:
            if player not in com1:
                com2.append(player)
        yield com1,com2

line1 = sys.stdin.readline().strip()
n = int(line1)

i=0
table = []
while(i<n):
    line2 = sys.stdin.readline().strip()
    table.append(list(map(int,line2.split())))
    i+=1

players=[i for i in range(n)]
min_gap = 100*n
for team1,team2 in divide_2_iter(players):
    t1_score,t2_score = 0,0
    for player1 in team1:
        for player2 in team1:
            if player1==player2:
                pass
            else:
                t1_score+=table[player1][player2]
    for player1 in team2:
        for player2 in team2:
            if player1==player2:
                pass
            else:
                t2_score+=table[player1][player2]
    if min_gap>abs(t1_score-t2_score):
        min_gap = abs(t1_score-t2_score)
print(min_gap)