import sys

input = sys.stdin.readline

n, values, cache, tot = int(input()), [int(i) for i in input().split()], {}, 0
for i in range(n):
    for j in range(i + 1, n):
        product = values[i] * values[j]
        if not product in cache:
            cache[product] = {-1: 0}
        if not i in cache[product]:
            cache[product][i] = 0
        if not j in cache[product]:
            cache[product][j] = 0
        tot += 8 * (cache[product][-1] - cache[product][i] - cache[product][j])
        cache[product][-1], cache[product][i], cache[product][j] = cache[product][-1] + 1, cache[product][i] + 1, cache[product][j] + 1
print(tot)