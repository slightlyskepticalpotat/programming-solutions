import math, sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    numbers = [int(i) for i in input().split()]
    print(math.ceil(sum(numbers) / x), sum([math.ceil(i / x) for i in numbers]))
