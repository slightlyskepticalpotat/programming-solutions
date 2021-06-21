import math, sys

input = sys.stdin.readline

def digit_sum(x):
    total = sum([int(char) for char in str(x)])
    return total

for _ in range(int(input())):
    n = int(input())
    for i in range(n, n + 3):
        if math.gcd(i, digit_sum(i)) > 1:
            print(i)
            break
