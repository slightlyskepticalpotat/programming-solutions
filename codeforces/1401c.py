import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    a, new = min(values), []
    for i in range(n):
        if not values[i] % a:
            new.append(values[i])
            values[i] = 0
    new.sort(reverse = True)
    values = [char if char else new.pop() for char in values]
    if values == list(sorted(values)):
        print("YES")
    else:
        print("NO")
