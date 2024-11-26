class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if (arr[i] * arr[i + 1] * arr[i + 2]) % 2:
                return True
        return False