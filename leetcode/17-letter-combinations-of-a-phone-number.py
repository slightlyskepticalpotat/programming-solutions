class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return
        text, ans = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}, [""]
        for i in digits:
            ans = [k + j for j in text[i] for k in ans]
        return ans