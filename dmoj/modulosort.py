import sys

input = sys.stdin.readline

m, k = int(input()), int(input())
integers = [int(i) for i in input().split()]

print(*sorted(integers, key = (lambda x: (x % k, x))))