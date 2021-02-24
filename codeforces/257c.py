import math

n, max_diff = int(input()), 0
values = [[int(i) for i in input().split()] for j in range(n)]
values = sorted([math.atan2(values[i][1], values[i][0]) for i in range(n)])
for i in range(n - 1):
    max_diff = max(max_diff, values[i + 1] - values[i])
max_diff = max(max_diff, 2 * math.pi - (values[-1] - values[0]))
print(360 - max_diff * 180 / math.pi)
