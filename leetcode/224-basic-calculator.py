class Solution:
    def calculate(self, s: str) -> int:
        ans, cur, stack, sign = 0, 0, [], 1
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in "+-":
                ans += cur * sign
                cur, sign = 0, (-1 if c == "-" else 1)
            elif c == "(":
                stack.append(ans)
                stack.append(sign) 
                ans, sign = 0, 1
            elif c == ")":
                ans, cur = ans + sign * cur, 0
                ans = ans * stack.pop() + stack.pop() # stack sign, ans
        return ans + cur * sign