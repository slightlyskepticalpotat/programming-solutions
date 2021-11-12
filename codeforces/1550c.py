import sys

input = sys.stdin.readline

def check(x):
    ans = x[0] <= x[1] <= x[2] or x[0] >= x[1] >= x[2]
    if len(x) == 4:
        ans |= x[1] <= x[2] <= x[3] or x[1] >= x[2] >= x[3]
        ans |= x[0] <= x[2] <= x[3] or x[0] >= x[2] >= x[3]
        ans |= x[0] <= x[1] <= x[3] or x[0] >= x[1] >= x[3]
    return not ans

for _ in range(int(input())):
    n, vals, ans = int(input()), [int(i) for i in input().split()], 0 # max 4
    ans += n # 1 long
    ans += n - 1 # 2 long
    for i in range(n - 2): # 3 long
        ans += check([vals[i], vals[i + 1], vals[i + 2]])
    for i in range(n - 3): # 4 long
        ans += check([vals[i], vals[i + 1], vals[i + 2], vals[i + 3]])
    print(ans)