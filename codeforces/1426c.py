for _ in range(int(input())):
    n, ans, i = int(input()), float("inf"), 1
    while i * i <= n:
        ans = min(ans, i - 1 + (n - 1) // i)
        i += 1
    print(ans)
