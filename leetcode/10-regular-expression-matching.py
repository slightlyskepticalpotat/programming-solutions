import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.match("^" + p + "$", s))