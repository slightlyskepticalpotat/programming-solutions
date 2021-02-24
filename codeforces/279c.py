import sys

input = sys.stdin.readline

n, m = map(int, input().split())
values, increase, decrease = [int(i) for i in input().split()], [0 for _ in range(n)], [0 for _ in range(n)]
for i in range(n - 2, -1, -1):
    if values[i] <= values[i + 1]:
        increase[i] = increase[i + 1] + 1
    else:
        increase[i] = 0
    if values[i] >= values[i + 1]:
        decrease[i] = decrease[i + 1] + 1
    else:
        decrease[i] = 0
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    if (a + increase[a]) >= b or (a + decrease[a]) >= b or (a + increase[a] + decrease[a + increase[a]]) >= b:
        print("Yes")
    else:
        print("No")
