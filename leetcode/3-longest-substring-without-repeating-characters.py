class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x, l, r, ans = set(), 0, 0, 0
        while r < len(s):
            if s[r] in x:
                x.remove(s[l])
                l += 1
            else:
                x.add(s[r])
                ans = max(ans, r - l + 1)
                r += 1
        return ans