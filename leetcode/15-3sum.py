class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, n, nums = set(), len(nums), sorted(nums)
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r: # can also manually increment indicies upon duplicate
                test = nums[i] + nums[l] + nums[r]
                if not test:
                    ans.add((nums[i], nums[l], nums[r]))
                    r, l = r - 1, l + 1
                elif test > 0:
                    r -= 1
                else:
                    l += 1
        return ans