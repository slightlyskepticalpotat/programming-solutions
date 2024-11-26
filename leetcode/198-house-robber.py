class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        dp = [nums[0], nums[1]] + [0 for i in range(len(nums) - 2)] # dp[i] max robbed up to house i
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2]  + nums[i])
        return dp[-1]