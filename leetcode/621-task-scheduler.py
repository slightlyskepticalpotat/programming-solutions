import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = [0 for i in range(26)]
        for i in tasks:
            cnt[ord(i) - 65] += 1
        top = max(cnt)
        top_cnt = len([i for i in cnt if i == top])
        return max(len(tasks), (top - 1) * (n + 1) + top_cnt)