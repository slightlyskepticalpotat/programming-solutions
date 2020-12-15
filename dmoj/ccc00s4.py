import sys

input = sys.stdin.readline

distance = int(input())
clubs, dp = [int(input()) for _ in range(int(input()))], [0 for i in range(distance + 1)]

for i in range(1, distance + 1):
    dp[i] = float("inf")
    for club in clubs:
        if i >= club:
            dp[i] = min(dp[i], dp[i - club] + 1)
if dp[-1] != float("inf"):
    print(f"Roberta wins in {dp[-1]} strokes.")
else:
    print("Roberta acknowledges defeat.")