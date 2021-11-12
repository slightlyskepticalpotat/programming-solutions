import math

for _ in range(int(input())):
    x, y = map(int, input().split())
    count = 0
    for i in range(1, math.ceil(math.sqrt(x))):
        count += max(0, min(y, x // i - 1) - i) # add the different slopes, then compensate (try desmos)
    print(count)
