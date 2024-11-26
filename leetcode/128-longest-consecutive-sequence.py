class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, ans = set(nums), 0
        for num in nums:
            if num - 1 not in nums:
                loc = 1
                while num + 1 in nums:
                    loc, num = loc + 1, num + 1
                ans = max(ans, loc)
        return ans