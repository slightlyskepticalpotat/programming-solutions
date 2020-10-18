import functools, math, sys

input = sys.stdin.readline

def lcm(x, y):
    return x * y // math.gcd(x, y)

for _ in range(int(input())):
    n, flag2, awake, asleep, offset = int(input()), False, [], [], []
    for i in range(n):
        a, s, o = map(int, input().split())
        awake.append(a)
        asleep.append(s)
        offset.append(o)
    period = functools.reduce(lcm, [awake[i] + asleep[i] for i in range(n)]) * 2
    for i in range(period):
        flag1 = True
        for j in range(n):
            if (i + offset[j]) % (awake[j] + asleep[j]) < awake[j]:
                flag1 = False
                break
        if flag1:
            print(i)
            flag2 = True
            break
    if not flag2:
        print("Foxen are too powerful")