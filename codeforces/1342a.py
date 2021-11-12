import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    print(min(abs(x - y) * a + min(x, y) * b, (x + y) * a))