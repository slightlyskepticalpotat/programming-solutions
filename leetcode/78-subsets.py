class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2 ** len(nums)):
            ans.append([nums[j] for j in range(len(nums)) if i & (1 << j)])
        return ans