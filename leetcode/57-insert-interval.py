class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, j = 0, 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            i += 1
        j = i
        
        while i < len(intervals) and newInterval[1] >= intervals[i][0]: # merge
            newInterval[0], newInterval[1] = min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])
            i += 1
        return intervals[:j] + [newInterval] + intervals[i:]