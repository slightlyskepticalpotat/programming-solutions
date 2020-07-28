import sys
input = sys.stdin.readline

def peers(x, y): # go in all 8 directions 
    peers = []
    if 0 <= x <= rows - 1 and 0 <= y + 1 <= columns - 1:
        peers.append(plan[x][y + 1])
    if 0 <= x <= rows - 1 and 0 <= y - 1 <= columns - 1:
        peers.append(plan[x][y - 1])
    if 0 <= x + 1 <= rows - 1 and 0 <= y <= columns - 1:
        peers.append(plan[x + 1][y])
    if 0 <= x - 1 <= rows - 1 and 0 <= y <= columns - 1:
        peers.append(plan[x - 1][y])
    if 0 <= x + 1<= rows - 1 and 0 <= y + 1 <= columns - 1:
        peers.append(plan[x + 1][y + 1])
    if 0 <= x + 1<= rows - 1 and 0 <= y - 1 <= columns - 1:
        peers.append(plan[x + 1][y - 1])
    if 0 <= x - 1 <= rows - 1 and 0 <= y + 1<= columns - 1:
        peers.append(plan[x - 1][y + 1])
    if 0 <= x - 1 <= rows - 1 and 0 <= y - 1<= columns - 1:
        peers.append(plan[x - 1][y - 1])
    return peers

plan = []
safe = 0
rows, columns = map(int, input().split())
for i in range(rows):
    plan.append([i for i in input().strip()])

for i in range(len(plan)):
    for j in range(len(plan[i])):
        if peers(i, j).count("S") < peers(i, j).count(".") and plan[i][j] != "S": # adjacent squares, as well as itself
            safe += 1
print(safe)