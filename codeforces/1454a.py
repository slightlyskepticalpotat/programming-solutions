for _ in range(int(input())):
    n = int(input())
    values = [int(i + 1) for i in range(n)]
    print(*([values[-1]] + values[:-1]))
