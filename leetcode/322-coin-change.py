class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for i in range(amount + 1)]
        for i in range(1, amount + 1):
            dp[i] = float("inf")
            for coin in coins:
                if i >= coin: # check coin size
                    dp[i] = min(dp[i], dp[i - coin] + 1) # fewer coins
        return dp[-1] if dp[-1] != float("inf") else -1