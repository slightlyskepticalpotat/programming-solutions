import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s, dp, ans = input().strip(), [1, 1], 0 # valid substrings ending in 0 or 1
    for char in s:
        if char == "?":
            ans += max(dp[0], dp[1])
            dp[0], dp[1] = dp[1] + 1, dp[0] + 1
        elif char == "0":
            ans += dp[0]
            dp[0], dp[1] = 1, dp[0] + 1
        elif char == "1":
            ans += dp[1]
            dp[0], dp[1] = dp[1] + 1, 1
    print(ans)
