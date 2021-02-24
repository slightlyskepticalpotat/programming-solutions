for _ in range(int(input())):
    n, values = int(input()), [int(i) for i in input().split()]
    best, ans = min(values), 0
    for i in range(n):
        if values[i] != best:
            ans += 1
    print(ans)
