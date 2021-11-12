import sys

input = sys.stdin.readline

for _ in range(int(input())):
    h, c, t = map(int, input().split())
    if t <= (h + c) / 2: # hc
        print(2)
    else: # hch
        ans = (h - t) // (2 * t - h - c)
        ans += int(abs((ans * (h + c) + h) - t * (2 * ans + 1)) * (2 * ans + 3) > abs(((ans + 1) * (h + c) + h) - t * (2 * ans + 3)) * (2 * ans + 1)) # precision errors are the worst
        print(2 * ans + 1)