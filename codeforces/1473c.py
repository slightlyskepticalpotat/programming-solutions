for _ in range(int(input())):
    n, k = map(int, input().split())
    values, inversions = [], 0
    for i in range(1, 2 * k - n):
        values.append(i)
    for i in range(k, 2 * k - n - 1, -1):
        values.append(i)
    print(*values)
