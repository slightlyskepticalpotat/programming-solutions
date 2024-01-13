class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for i in magazine:
            if not letters.get(i, 0):
                letters[i] = 0
            letters[i] += 1
        for i in ransomNote:
            if not letters.get(i, 0):
                return False
            letters[i] -= 1
        return True