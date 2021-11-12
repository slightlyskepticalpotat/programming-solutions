import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    j = min(m, n // k) # winner
    left = math.ceil((m - j) / (k - 1)) # runner-up
    print(j - left)