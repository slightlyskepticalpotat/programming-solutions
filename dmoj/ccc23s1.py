import sys

input = sys.stdin.readline

c, ans, loc = int(input()), 0, 0
row_a, row_b = [int(i) for i in input().split()], [int(i) for i in input().split()]
for i in range(c):
    if row_a[i]:
        if not loc:
            loc += 3
        else:
            loc += 1
    else:
        if loc:
            ans += loc
            loc = 0
if loc and loc < 3:
    loc += 1
ans += loc
loc = 0
for i in range(c):
    if row_b[i]:
        if not loc:
            loc += 3
        else:
            loc += 1
    else:
        if loc:
            ans += loc
            loc = 0
if loc and loc < 3:
    loc += 1
ans += loc
loc = 0
for i in range(c):
    if row_a[i] and row_b[i] and (i + 1) % 2:
        ans -= 2
print(ans)
