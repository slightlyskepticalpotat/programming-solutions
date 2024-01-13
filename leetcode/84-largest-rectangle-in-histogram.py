class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights, ans, stack = heights + [0], 0, [-1] # idx of tallest
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]: # current height lower
                ans = max(ans, heights[stack.pop()] * (i - stack[-1] - 1)) # h * w
            stack.append(i)
        return ans