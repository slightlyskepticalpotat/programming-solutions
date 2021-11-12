import sys

input = sys.stdin.readline

def dfs(start):
    if start not in searched:
        searched.add(start)
        for i in range(n):
            if start[0] == piles[i][0] or start[1] == piles[i][1]: # follow the axes
                dfs(piles[i])

n, num_piles, piles, searched = int(input()), 0, [], set()
for _ in range(n):
    a, b = map(int, input().split())
    piles.append((a, b))
for i in range(n):
    if piles[i] not in searched:
        num_piles += 1
        dfs(piles[i])
print(num_piles - 1)
