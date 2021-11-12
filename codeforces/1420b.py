for _ in range(int(input())):
    n, values, ans = int(input()), [int(i) for i in input().split()], 0
    for i in range(29, -1, -1): # log2(10 ** 5)
        loc = 0
        for j in range(n):
            if 2 ** i <= values[j] < 2 ** (i + 1): # same highest set bit
                loc += 1
        ans += (loc * (loc - 1)) // 2
    print(ans)
