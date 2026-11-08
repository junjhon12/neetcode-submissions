class MedianFinder:

    def __init__(self):
        # self.small is a max-heap (simulated using negative numbers)
        self.small = []
        # self.large is a standard min-heap
        self.large = []

    def addNum(self, num: int) -> None:
        # Push to the max-heap (small half)
        heapq.heappush(self.small, -num)
        
        # Ensure every element in small is <= every element in large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Maintain size property: small can have at most 1 more element than large
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
        
        