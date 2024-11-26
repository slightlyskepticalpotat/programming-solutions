class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum, minimum, ans = 1, 1, nums[0]
        for i in nums:
            test = (i, i * maximum, i * minimum)
            maximum, minimum = max(test), min(test)
            ans = max(ans, maximum)
        return ans