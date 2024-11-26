class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            i = abs(num)
            if nums[i] < 0:
                return i
            nums[i] *= -1
        return len(nums)