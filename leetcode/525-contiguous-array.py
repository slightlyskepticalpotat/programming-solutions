class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans, cnt, start = 0, 0, {} # smallest value such that 1-0=x
        for i in range(len(nums)):
            cnt = cnt + 1 if nums[i] else cnt - 1
            if not cnt: # balanced ones and zeroes
                ans = i + 1
            elif cnt in start:
                ans = max(ans, i - start[cnt])
            else:
                start[cnt] = i
        return ans