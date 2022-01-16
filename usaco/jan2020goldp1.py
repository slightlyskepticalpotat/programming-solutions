import sys

sys.stdin = open("time.in", "r")
sys.stdout = open("time.out", "w")

n, m, c = map(int, input().split())
moonies, roads, dp, ans = [int(i) for i in input().split()], {i: [] for i in range(n)}, [[-1 for i in range(n)] for j in range(1001)], 0 # dp[i][j] is maximum amount after i days ending at city j
dp[0][0] = 0
for _ in range(m):
    a, b = map(int, input().split())
    roads[a - 1].append(b - 1) # city numbers reduced by 1

for i in range(1000):
    for j in range(n):
        if dp[i][j] != -1: # previously reached
            for peer in roads[j]:
                dp[i + 1][peer] = max(dp[i + 1][peer], dp[i][j] + moonies[peer])
    ans = max(ans, dp[i][0] - c * i ** 2)
print(ans)
