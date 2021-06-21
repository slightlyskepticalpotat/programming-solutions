import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values, dp, cnt = int(input()), [int(i) for i in input().split()], [], {}
    for i in range(n):
        dp.append(dp[i - 1] if dp else 0) # dp[i] is sum of weight ending at i
        if values[i] in cnt: # cnt[i] is sum of indicies of i
            dp[i] += cnt[values[i]] # add if previously seen
        cnt[values[i]] = cnt.get(values[i], 0) + i + 1
    print(sum(dp))
