import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    best, count = float("inf"), 0
    if b == 1:
        b += 1
        count += 1
    for i in range(30): # log2
        copy_a, loc = a, 0
        while copy_a:
            copy_a //= (b + i)
            loc += 1
        best = min(best, loc + count + i)
    print(best)
