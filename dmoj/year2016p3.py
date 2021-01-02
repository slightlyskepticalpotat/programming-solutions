import bisect, sys

input = sys.stdin.readline

n, snowballs, best = int(input()), [int(i) for i in input().split()], 0
snowballs.sort()
for i in range(n):
    for j in range(i + 1, n):
        a, b = snowballs[i], snowballs[j]
        try:
            if snowballs[bisect.bisect_left(snowballs, b + (b - a), j + 1, n)] == b + (b - a):
                best = max(best, 3 * b)
        except:
            pass
print(best)