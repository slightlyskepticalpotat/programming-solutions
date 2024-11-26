class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        long = [prices[i + 1] - prices[i] if prices[i] < prices[i + 1] else 0 for i in range(len(prices) - 1)] 
        return sum(long)