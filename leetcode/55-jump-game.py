class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum = 0 # max index we can reach
        for i, n in enumerate(nums):
            if maximum < i:
                return False
            maximum = max(maximum, i + n)
        return True