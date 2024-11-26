class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans, stack = [0 for i in range(len(temperatures))], [] # current best temperature
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t: 
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans