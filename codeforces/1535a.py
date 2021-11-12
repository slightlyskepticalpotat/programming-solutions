import sys

input = sys.stdin.readline

for _ in range(int(input())):
    players = [int(i) for i in input().split()]
    fair_match = list(sorted(players, reverse=True))[:2]
    real_match = sorted([max(players[0], players[1]), max(players[2], players[3])], reverse=True)
    if fair_match == real_match:
        print("YES")
    else:
        print("NO")
