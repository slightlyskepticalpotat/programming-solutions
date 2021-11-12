import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, y, k = map(int, input().split())
    print((k + k * y + x - 3) // (x - 1) + k)
    # precision, math.ceil(a / b) == math.floor((a + b - 1) / b)
