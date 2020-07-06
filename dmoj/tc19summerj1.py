m, n = map(int, input().split())
dist = []
while m:
    dist.append(m - n)
    m //= 2
dist = sorted(dist, key=abs)
print(n + dist[0])