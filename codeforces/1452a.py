for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == y:
        print(x + y)
    else:
        print(2 * min(x, y) + 2 * (max(x, y) - min(x, y)) - 1)
