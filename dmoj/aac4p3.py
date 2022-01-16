import math, sys

input = sys.stdin.readline

n, m = map(int, input().split())
points = [[int(i) for i in input().split()] for j in range(n)]
slopes = [[int(i) for i in input().split()] for j in range(m)]
seen, ans, new_slopes = set(), 0, []
for slope in slopes:
    if slope[0] / slope[1] not in seen:
        seen.add(slope[0] / slope[1])
        new_slopes.append(slope)
for slope in new_slopes:
    loc = {}
    for point in points:
        idx = slope[0] * point[0] - slope[1] * point[1]
        loc[idx] = loc.get(idx, 0) + 1
    for i in loc:
        ans += math.comb(loc[i], 2)
print(ans)