class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        total //= 2
        dp = [1] + [0 for i in range(total)]
        for num in nums:
            for i in range(total, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[-1]