import sys

input = sys.stdin.readline

for _ in range(5):
    r, c, ro = map(int, input().split())
    danger_r, danger_c = set(), set()
    board, safe = [[0] * c] * r, 0

    for i in range(ro):
        a, b = map(int, input().split())
        danger_r.add(a - 1)
        danger_c.add(b - 1)

    safe = (r - len(danger_r)) * (c - len(danger_c))
    print(safe)