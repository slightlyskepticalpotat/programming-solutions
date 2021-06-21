for _ in range(int(input())):
    n, values, ans = int(input()), [int(i) for i in input().split()], 0
    for i in range(1, n):
        low, top = min(values[i], values[i - 1]), max(values[i], values[i - 1])
        while low * 2 < top:
            low *= 2
            ans += 1
    print(ans)
