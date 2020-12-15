import sys

input = sys.stdin.readline

n, m = map(int, input().split())
colours, relatives = [int(i) for i in input().split()], [[int(i) for i in input().split()] for _ in range(m)]
left, right, best = [-1 for i in range(1000001)], [-1 for i in range(1000001)], 0

for i in range(n):
    if left[colours[i]] == -1:
        left[colours[i]] = i
for i in range(n, -1, -1):
    if right[colours[i - 1]] == -1:
        right[colours[i - 1]] = i
for relative in relatives:
    if left[relative[0]] != -1 and right[relative[1]] != -1:
        best = max(best, right[relative[1]] - left[relative[0]])
print(best)