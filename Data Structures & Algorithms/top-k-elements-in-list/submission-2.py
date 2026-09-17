class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for number in nums:
            count[number] = count.get(number, 0) + 1
        sorted_elements = sorted(count, key=count.get, reverse=True)
        return sorted_elements[:k]