import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a_0, a_1, a_2 = map(int, input().split())
    b_0, b_1, b_2 = map(int, input().split())
    # 0, 2
    m = min(a_0, b_2)
    a_0 -= m
    b_2 -= m
    # 1, 0
    m = min(a_1, b_0)
    a_1 -= m
    b_0 -= m
    # 2, 1
    m = min(a_2, b_1)
    a_2 -= m
    b_1 -= m
    ans = 2 * m
    # 1, 2
    print(ans - 2 * min(a_1, b_2))
