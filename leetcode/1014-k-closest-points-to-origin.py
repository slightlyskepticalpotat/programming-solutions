import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[math.sqrt(point[0] ** 2 + point[1] ** 2), point] for point in points]
        points.sort()
        return [point[1] for point in points][:k]