class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if all(num == 0 for num in nums1) and all(num == 0 for num in nums2): return 0
        new_list = sorted(nums1 + nums2)
        mid = len(new_list) // 2
        if len(new_list) % 2 == 0:
            mid_left = mid - 1
            mid_right = mid
            return (new_list[mid_left] + new_list[mid_right]) / 2
        return float(new_list[mid])
