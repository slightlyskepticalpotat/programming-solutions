import math, sys

input = sys.stdin.readline

def factors(x):
    factors = set()
    for i in range(1, math.floor(math.sqrt(x)) + 1):
        if not x % i:
            factors.add(i)
            factors.add(x // i)
    return factors

def generate(start, diff):
    seq = [start]
    for i in range(n - 1):
        seq.append(seq[-1] + diff)
    return seq

for _ in range(int(input())):
    n, x, y = map(int, input().split())
    working = [generate(j, i) for i in factors(y - x) for j in range(1, 51)]
    print(*min([i for i in working if x in i and y in i], key = lambda x: max(x)))
