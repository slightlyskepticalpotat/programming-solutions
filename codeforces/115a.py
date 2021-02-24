import sys

input = sys.stdin.readline

n = int(input())
costs, plan = [0 for _ in range(n)], {i: int(input()) - 1 for i in range(n)}
for i in range(n):
    dist = 0
    curr = plan[i]
    while True:
        if curr == -2:
            break
        dist += 1
        costs[curr] = max(costs[curr], dist)
        curr = plan[curr]
print(max(costs) + 1)
