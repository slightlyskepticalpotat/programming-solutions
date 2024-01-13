from collections import deque 

class Solution: # classic bfs with wildcards
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        q, chars = deque([[beginWord, 1]]), set("".join(wordList))
        while q:
            word, step = q.popleft()
            step += 1
            for i in range(len(beginWord)):
                for c in chars:
                    nextWord = word[:i] + c + word[i + 1:]
                    if nextWord == endWord:
                        return step
                    if nextWord in wordList:
                        q.append([nextWord, step])
                        wordList.remove(nextWord)
        return 0