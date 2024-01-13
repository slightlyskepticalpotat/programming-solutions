class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(reverse = True)
        new = [intervals.pop()]
        while intervals:
            if new[-1][1] >= intervals[-1][0]:
                new[-1][1] = max(new[-1][1], intervals[-1][1])
                intervals.pop()
                continue
            new.append(intervals.pop())
        return new