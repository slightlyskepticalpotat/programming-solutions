for _ in range(int(input())):
    n = int(input())
    plan = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        plan[i][i] = 1
        plan[i][n - i - 1] = 1
    if n % 2:
        plan[n // 2][n // 2 + 1] = 1
        plan[n // 2 + 1][n // 2] = 1
    for row in plan:
        print(*row)
