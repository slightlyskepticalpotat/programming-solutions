import math, sys

input = sys.stdin.readline

def factors(x):
    factors = set()
    for i in range(1, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            factors.add(i)
            factors.add(x // i)
    return list(factors)

for _ in range(int(input())):
    n, values, working = int(input()), [int(i) for i in input().split()], []
    to_check, total = factors(sum(values)), sum(values)

    for i in range(len(to_check)): # greedily check factors
        target, current, array, steps = to_check[i], 0, [], 0
        i = 0
        while i < n:
            current += values[i]
            if current > target:
                break
            elif current == target:
                array.append(current)
                current = 0
            else:
                steps += 1
            i += 1
        if sum(array) == total:
            working.append(steps)
    print(min(working))
