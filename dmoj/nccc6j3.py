import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    max = 0
    for i in range(c // a + 1):
        check = i * a + (c - i * a) // b * b
        if max < check:
            max = check
    if max == c:
        print("YES")
    else:
        print("NO")