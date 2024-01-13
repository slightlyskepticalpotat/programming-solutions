class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1                
        for j in t:
            if not freq.get(j, 0):
                return False
            freq[j] -= 1
        for k in freq:
            if freq[k]:
                return False
        return True