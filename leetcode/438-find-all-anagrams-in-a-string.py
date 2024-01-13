from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt, ans = defaultdict(int), []
        if len(p) > len(s):
            return ans
        for char in p:
            cnt[char] += 1
        for i in range(len(p)):
            if s[i] in cnt: # only care about letters in p
                cnt[s[i]] -= 1
        for i in range(len(s) - len(p) + 1):
            if not any(cnt.values()):
                ans.append(i)
            if s[i] in cnt:
                cnt[s[i]] += 1
            if i + len(p) < len(s):
                if s[i + len(p)] in cnt:
                    cnt[s[i + len(p)]] -= 1
        return ans