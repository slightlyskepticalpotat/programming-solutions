import sys

input = sys.stdin.readline

n, m = map(int, input().split())
costs = [[int(i)] for i in input().split()]
costs = [costs[j] + [j] for j in range(n)]
costs2 = {x: y for y, x in costs}
costs.sort(reverse = True)
connections = {i: [] for i in range(n)}
total = 0
for i in range(m):
    a, b = map(int, input().split())
    connections[a - 1].append(b - 1)
    connections[b - 1].append(a - 1)
for i in range(n):
    while connections[costs[i][1]]:
        current = connections[costs[i][1]].pop()
        connections[current].remove(costs[i][1])
        total += costs2[current]
print(total)
