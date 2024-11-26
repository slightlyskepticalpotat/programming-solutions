class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = sorted([[abs(i - x), i] for i in arr])
        return sorted([i[1] for i in arr[:k]])