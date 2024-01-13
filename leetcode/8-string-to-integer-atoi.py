class Solution:
    def myAtoi(self, s: str) -> int:
        sig, res, s = 1, "0", s.strip()
        if not s:
            return 0
        if s[0] in ["-", "+"]:
            if s[0] == "-":
                sig *= -1
            s = s[1:]
        for i in range(len(s)):
            if s[i] in "0123456789":
                res += s[i]
            else:
                break
        res = int(res) * sig
        return min(max(res, -2 ** 31), 2 ** 31 - 1) # clamp