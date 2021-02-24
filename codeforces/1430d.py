import math

for _ in range(int(input())):
    n, s, step1, step2 = int(input()), [char for  char in input().strip()], 0, 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            step1 += 1
            step1 = min(step1, step2)
        else:
            step2 += 1
    print(step1 + math.ceil((step2 - step1) / 2))
