class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x == int(str(abs(x))[::-1])