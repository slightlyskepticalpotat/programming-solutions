from bisect import bisect

class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None: # calls strictly incr
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        i = bisect(self.data[key], timestamp, key = lambda x: x[0])
        return self.data[key][i - 1][1] if i else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)