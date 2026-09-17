class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return None

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        count = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                count += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                count += right_max - height[right]
        return count