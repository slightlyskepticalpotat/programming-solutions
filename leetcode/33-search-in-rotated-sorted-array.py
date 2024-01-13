class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[low] <= nums[mid]: # pivot is to right, left is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else: # pivot is to left, right is sorted
                if nums[high] >= target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            if nums[mid] == target:
                return mid
        return -1