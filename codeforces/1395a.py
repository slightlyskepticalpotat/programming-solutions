import sys

input = sys.stdin.readline

for _ in range(int(input())):
    r, g, b, w = map(int, input().split())
    m, ans = min(min(r, g, b), 1), False # subtract one if possible
    ans |= sum([i % 2 for i in [r, g, b, w]]) < 2 # one or zero odd
    r, g, b, w = r - m, g - m, b - m, w + 3 * m
    ans |= sum([i % 2 for i in [r, g, b, w]]) < 2 # one or zero odd
    if ans:
        print("Yes")
    else:
        print("No")
