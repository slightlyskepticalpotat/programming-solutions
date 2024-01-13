class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap, profit = float("inf"), -float("inf")
        for i in prices:
            cheap = min(cheap, i)
            profit = max(profit, i - cheap)
        return profit