class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            hours_spent = 0
            for pile in piles:
                hours_spent += (pile + mid - 1) // mid
            if hours_spent <= h:
                right = mid
            else:
                left = mid + 1
        return left