for _ in range(int(input())):
    n = int(input())
    sequence = [int(i) for i in input().split()]
    dp = [-1 for i in range(n)]
    
    for i in range(n - 1, -1, -1):
        dp[i] = sequence[i]
        if i + sequence[i] < n:
            dp[i] += dp[i + sequence[i]]
    print(max(dp))
