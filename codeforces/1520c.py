import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, index = int(input()), 1
    if n == 2:
        print(-1)
    else:
        matrix = [[-1 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if (i + j) % 2:
                    matrix[i][j] = index
                    index += 1
        for i in range(n):
            for j in range(n):
                if not (i + j) % 2:
                    matrix[i][j] = index
                    index += 1
        for row in matrix:
            print(*row)
