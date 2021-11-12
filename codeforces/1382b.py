import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals = int(input()), [int(i) for i in input().split()]
    if n % 2: # all 1's
        ans = "First"
    else:
        ans = "Second"
    for i in range(n):
        if vals[i] > 1:
            if i % 2:
                ans = "Second"
            else:
                ans = "First"
            break
    print(ans)
