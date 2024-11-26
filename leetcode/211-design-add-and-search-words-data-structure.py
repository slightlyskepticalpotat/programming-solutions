class WordDictionary:

    def __init__(self):
        self.words = set()

    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        cnt = word.count(".")
        if not cnt:
            return word in self.words
        elif cnt == 1:
            i = word.index(".")
            search = [word[:i] + char + word[i + 1:] for char in "abcdefghijklmnopqrstuvwxyz"]
            return any(w in self.words for w in search)
        else: # at most two dots
            i = word.index(".")
            search, search2 = [word[:i] + char + word[i + 1:] for char in "abcdefghijklmnopqrstuvwxyz"], []
            for w in search:
                j = w.index(".")
                search2.extend([w[:j] + char + w[j + 1:] for char in "abcdefghijklmnopqrstuvwxyz"])
            return any(w in self.words for w in search2)      

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)