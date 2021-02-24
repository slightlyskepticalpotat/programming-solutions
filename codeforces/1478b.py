# since d < 10, we can always end up with dn where n is another digit if values[i] >= 10 * d

for _ in range(int(input())):
    q, d = map(int, input().split())
    values, scale = [int(i) for i in input().split()], 10 * d
    dp = [0 for i in range(scale + 1)]
    dp[0], i = 1, 0
    while 10 * i + d <= scale:
        j = 0
        while 10 * i + j + d <= scale:
            dp[10 * i + j + d] = max(dp[10 * i + j + d], dp[j])
            j += 1
        i += 1
    for i in range(q):
        if values[i] >= scale or dp[values[i]]:
            print("YES")
        else:
            print("NO")
