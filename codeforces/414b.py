n, k = map(int, input().split())
dp, total = [[0 for i in range(n + 1)] for j in range(k + 1)], 0 # dp[len][max]

for i in range(n + 1): # when the max is 1 there is only 1 sequence
    dp[1][i] = 1
for i in range(2, k + 1): # higher maximum value
    for j in range(1, n + 1): # longer length
        for kk in range(j, n + 1, j): # follow the factors
            dp[i][kk] = (dp[i][kk] + dp[i - 1][j]) % 1000000007
for i in range(1, n + 1): # add all the sequences of length k
    total = (total + dp[k][i]) % 1000000007
print(total)
