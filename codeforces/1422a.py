for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(max(max(a, b), c) + 1)
