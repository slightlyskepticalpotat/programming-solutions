import math, sys

input = sys.stdin.readline

def goods(x):
    good = 0
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if math.gcd(x[i], 2 * x[j]) > 1:
                good += 1
    return good

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    ordered = [i for i in vals if not i % 2] + [i for i in vals if i % 2]
    print(goods(ordered))
