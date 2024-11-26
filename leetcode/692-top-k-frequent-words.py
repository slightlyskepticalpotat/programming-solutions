from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = defaultdict(int)
        for word in words:
            cnt[word] -= 1 # reverse sort
        cnt = sorted([[cnt[i], i] for i in cnt])[:k]
        return [i[1] for i in cnt]