class Solution:
    def process(self, height):
        i, start, ans, loc = 0, 0, 0, 0
        while i < len(height):
            if height[i] >= start:
                ans, loc, start = ans + loc, 0, height[i] # new bucket
            else:
                loc += (start - height[i])
            i += 1
        return ans

    def trap(self, height: List[int]) -> int:
        max_i = height.index(max(height))
        return self.process(height[:max_i + 1]) + self.process(height[max_i:][::-1])
