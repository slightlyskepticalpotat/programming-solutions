for _ in range(int(input())):
    n, ans = int(input()), []
    if n % 2:
        ans  = 10000 * [1, -1]
        print(*ans[:(n * (n - 1)) // 2])
    else:
        for i in range(n):
            for j in range(i + 1, n):
                if j - i > n // 2:
                    ans.append(-1)
                elif j - i == n // 2:
                    ans.append(0)
                elif j - i < n // 2:
                    ans.append(1)
        print(*ans)
