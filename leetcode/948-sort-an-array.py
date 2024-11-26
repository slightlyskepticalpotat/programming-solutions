class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        freq, ans = {i: 0 for i in range(-50000, 50001)}, []
        for i in nums:
            freq[i] += 1
        for k, v in freq.items():
            ans.extend([k] * v)
        return ans