import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    squares, y, ans = [[i for i in input().strip()] for j in range(n)], min(y, 2 * x), 0
    for i in range(n):
        for j in range(m - 1):
            if squares[i][j] == "." == squares[i][j + 1] == ".":
                squares[i][j] = "*"
                squares[i][j + 1] = "*"
                ans += y
            elif squares[i][j] == ".":
                squares[i][j] = "*"
                ans += x
        if squares[i][-1] == ".": # last one left
            squares[i][-1] = "*"
            ans += x
    print(ans)