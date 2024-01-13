class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = [int(i) for i in a], [int(i) for i in b]
        carry, ans = 0, ""
        while a or b or carry:
            if a:
                carry += a.pop()
            if b:
                carry += b.pop()
            carry, result = divmod(carry, 2)
            ans = str(result) + ans
        return ans