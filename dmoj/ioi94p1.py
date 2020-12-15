# maximal path sum

import sys

input = sys.stdin.readline

n = int(input())
triangle = [[int(i) for i in input().split()] + [0] * (n - i - 1) for i in range(n)] # squares are triangles too, pad with zeros
triangle = [list(row) for row in zip(*triangle[::-1])]
triangle = [list(row) for row in zip(*triangle[::-1])]

for i in range(1, n):
    for j in range(i, n):
        triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1]) # top and top left
print(triangle[-1][-1])