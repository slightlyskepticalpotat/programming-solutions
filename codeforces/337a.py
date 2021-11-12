n, m = map(int, input().split())
values, best = [int(i) for i in input().split()], float("inf")
values.sort()
for i in range(n, m + 1):
    if values[i - 1] - values[i - n] < best:
        best = values[i - 1] - values[i - n]
print(best)
