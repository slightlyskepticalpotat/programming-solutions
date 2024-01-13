class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        for i in range(0, len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True