import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    odd, even = [char for char in values if char % 2], [char for char in values if not char % 2]
    print(*(odd + even))
