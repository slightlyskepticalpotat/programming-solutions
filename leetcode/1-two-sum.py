class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(len(nums)):
            if idx.get(target - nums[i], -1) != -1:
                return [idx[target - nums[i]], i]
            idx[nums[i]] = i