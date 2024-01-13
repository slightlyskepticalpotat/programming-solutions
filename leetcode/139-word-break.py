import functools

class Solution:
    @cache
    def test(self, s):
            if s in self.words:
                return True
            return any(s[:i] in self.words and self.test(s[i:]) for i in range(len(s)))

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.words = set(wordDict)
        return self.test(s)