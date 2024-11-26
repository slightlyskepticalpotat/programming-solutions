class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = {}
        for i in word:
            freq[i] = freq.get(i, 0) + 1
        freq = list(freq.values())
        for i in range(len(freq)):
            freq[i] -= 1
            if min(i for i in freq if i) == max(i for i in freq if i):
                return True
            freq[i] += 1
        return False