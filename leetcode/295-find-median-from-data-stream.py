import heapq

class MedianFinder:
    def __init__(self):
        self.p, self.q = [], [] # for smaller and larger halves

    def addNum(self, num: int) -> None:
        if not self.p or num < -self.p[0]:
            heapq.heappush(self.p, -num)
        else:
            heapq.heappush(self.q, num)
        if len(self.p) - len(self.q) > 1:
            heapq.heappush(self.q, -heapq.heappop(self.p))
        elif len(self.q) - len(self.p) > 1:
            heapq.heappush(self.p, -heapq.heappop(self.q))

    def findMedian(self) -> float:
        if len(self.p) == len(self.q):
            return (self.q[0] - self.p[0]) / 2
        return -self.p[0] if len(self.p) > len(self.q) else self.q[0]
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()