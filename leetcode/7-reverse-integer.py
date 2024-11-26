from math import copysign 

class Solution:
    def reverse(self, x: int) -> int:
        return int(copysign(int(str(abs(x))[::-1]), x)) if -2**31 <= int(copysign(int(str(abs(x))[::-1]), x)) <= 2**31-1 else 0