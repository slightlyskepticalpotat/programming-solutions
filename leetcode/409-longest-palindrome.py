class Solution:
    def longestPalindrome(self, s: str) -> int:
        count, ans, flag = {}, 0, 0
        for i in s:
            if not count.get(i, 0):
                count[i] = 0
            count[i] += 1
            
        for i in count:
            if count[i] % 2:
                flag = 1
            ans += count[i] // 2 * 2
        return ans + flag