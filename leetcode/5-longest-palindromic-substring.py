class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_start, ans_end, n = 0, 1, len(s)
        dp = [[False] * n for j in range(n)] # dp[i][j] longest palindrome from i to j
        for i in range(n):
            dp[i][i] = True
        for i in range(n): # end
            for j in range(i): # start
                if s[j] == s[i] and (dp[j + 1][i - 1] or i == j + 1):
                    dp[j][i] = True
                    if i - j + 1 > ans_end - ans_start: # if longer
                        ans_start, ans_end = j, i + 1
        return s[ans_start:ans_end]