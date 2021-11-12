# wacky array overflowing

m, t, r = map(int, input().split())
ghosts = [int(i) for i in input().split()]
candles, flag = [0 for _ in range(ghosts[-1] + 1 + 300)], True
for i in range(m):
    now = 0
    for j in range(ghosts[i] - 1, ghosts[i] - t - 1, -1):
        now += candles[j]
    if now < r:
        for j in range(ghosts[i] - 1, ghosts[i] - t - 1, -1):
            if not candles[j] and now < r:
                candles[j] = 1
                now += 1
    if now < r:
        flag = False
if flag:
    print(sum(candles))
else:
    print(-1)
