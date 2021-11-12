import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    print(100 // math.gcd(k, 100))
