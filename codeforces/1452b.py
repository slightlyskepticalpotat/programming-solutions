# expected value 

import math

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    blocks = max(math.ceil(sum(values) / (n - 1)), max(values))
    print((n - 1) * blocks - sum(values))
