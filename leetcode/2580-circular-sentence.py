class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = [i for i in sentence.split()]
        return all([True if words[i][-1] == words[i + 1][0] else False for i in range(len(words) - 1)] + [words[-1][-1] == words[0][0]])