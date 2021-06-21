import math, sys

input = sys.stdin.readline

def mex(x):
    i = 0
    while i in x:
        i += 1
    return i

for _ in range(int(input())):
    n, k = map(int, input().split())
    numbers = set([int(i) for i in input().split()])
    if not k:
        print(n)
    elif mex(numbers) == max(numbers) + 1: # new number each time
        print(n + k)
    else: # mex(numbers) is constant
        numbers.add(math.ceil((max(numbers) + mex(numbers)) / 2))
        print(len(numbers))
