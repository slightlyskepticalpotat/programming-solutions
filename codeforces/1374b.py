import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, threes = int(input()), 0
    while not n % 3:
        n, threes = n / 3, threes + 1
    twos = math.log2(n)
    if twos != twos // 1 or twos > threes: # has other factors
        print(-1)
    else:
        print(threes + (threes - int(twos)))
