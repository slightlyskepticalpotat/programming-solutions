import sys

input = sys.stdin.readline
sys.setrecursionlimit(65536)

def dfs(start):
    ans = 0
    for peer in blocks[start]:
        if not blocks[peer]:
            ans += 1
        else:
            ans += 1
            ans += dfs(peer)
    return ans

n, north, east = int(input()), [], []
for i in range(n):
    direction, x, y = input().split()
    if direction == "N":
        north.append([int(x), int(y), i, 0, True])
    else:
        east.append([int(x), int(y), i, 0, True])
north.sort(key = lambda x: x[0])
east.sort(key = lambda x: x[1])
blocks = {i: [] for i in range(n)}

for i in range(len(north)):
    for j in range(len(east)):
        x_diff = north[i][0] - east[j][0]
        y_diff = east[j][1] - north[i][1]
        if x_diff < 0 or y_diff < 0:
            pass
        else:
            if x_diff < y_diff and east[j][4] and north[i][4]:
                north[i][4] = False
                blocks[east[j][2]].append(north[i][2]) # east blocks north
            elif y_diff < x_diff and north[i][4] and east[j][4]:
                east[j][4] = False
                blocks[north[i][2]].append(east[j][2]) # north blocks east
for i in range(n):
    print(dfs(i))
