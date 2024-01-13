class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        dp = [(0, 0)] # [x, y] means max profit y for x end time
        for s, e, p in jobs:
            i = bisect.bisect(dp, (s + 1,)) - 1 # proper start time
            new_p = dp[i][1] + p # max profit from before + this job
            if new_p > dp[-1][1]: # vs maximum profit without job
                dp.append((e, new_p))
        return dp[-1][1]