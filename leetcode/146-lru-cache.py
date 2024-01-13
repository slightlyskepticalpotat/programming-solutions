class LRUCache:

    def __init__(self, capacity: int):
        self.cache, self.capacity = {}, capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache[key] = self.cache.pop(key) # reinsert
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.pop(next(iter(self.cache))) # returns fifo
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)