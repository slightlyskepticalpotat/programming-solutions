from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freqs, self.freq_n, self.top = defaultdict(int), defaultdict(list), 0

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        self.freq_n[self.freqs[val]].append(val)
        self.top = max(self.top, self.freqs[val])

    def pop(self) -> int:
        new_ret = self.freq_n[self.top].pop()
        self.freqs[new_ret] -= 1
        if not self.freq_n[self.top]:
            self.top -= 1
        return new_ret


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()