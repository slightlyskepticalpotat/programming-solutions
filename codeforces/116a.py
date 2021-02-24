n, tram, best = int(input()), 0, 0
for i in range(n):
    a, b = map(int, input().split())
    tram -= a
    tram += b
    if tram > best:
        best = tram
print(best)
