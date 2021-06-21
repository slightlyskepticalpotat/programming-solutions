import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    available = [[int(i) for i in input().split()][1:] for j in range(m)]
    playing, played = [available[i][0] for i in range(m)], {i + 1: 0 for i in range(n)}
    for i in range(m):
        played[playing[i]] += 1
    to_replace = list(sorted([player for player in played], key = lambda x: played[x]))[-1]
    if played[to_replace] > math.ceil(m / 2):
        for i in range(m):
            if playing[i] == to_replace:
                for player in available[i]:
                    if player != to_replace and played[player] + 1 <= math.ceil(m / 2): # we can replace
                        playing[i] = player
                        played[player] += 1
                        played[to_replace] -= 1
                        break
    if played[to_replace] <= math.ceil(m / 2):
        print("YES")
        print(*playing)
    else:
        print("NO")
