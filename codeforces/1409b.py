import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, x, y, n = map(int, input().split())
    a_first_a, a_first_b = min(a - x, n), min(n - min(a - x, n), b - y)
    b_first_a, b_first_b = min(n - min(b - y, n), a - x), min(b - y, n)
    print(min((a - a_first_a) * (b - a_first_b), (a - b_first_a) * (b - b_first_b)))
