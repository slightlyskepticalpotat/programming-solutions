class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, mid, high = 0, -1, len(nums)
        while low < high:
            mid = (high + low) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
        if nums[min(low, len(nums) - 1)] == target:
            return low
        return -1