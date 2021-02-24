import math

for _ in range(int(input())):
    n = int(input())
    max_pos = math.floor(math.sqrt(n - 1 + n))
    print((max_pos - int(not max_pos % 2)) // 2)
