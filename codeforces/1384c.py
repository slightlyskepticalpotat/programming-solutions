import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b, ans = int(input()), [char for char in input().strip()], [char for char in input().strip()], 0
    for i in range(n):
        if a[i] > b[i]:
            ans = -1
    if ans != -1:
        for char in "abcdefghijklmnopqrst": # iterate over each b[i] we convert to
            s = set()
            for i in range(n):
                if char == b[i] and a[i] < b[i]:
                    s.add(a[i])
            for i in range(n):
                if a[i] in s:
                    a[i] = char
            ans += len(s)
    print(ans)
