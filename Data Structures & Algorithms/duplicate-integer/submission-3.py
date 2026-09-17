class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0: return False
        nums = sorted(nums)
        for current_num, next_num in zip(nums, nums[1:]):
            if current_num == next_num:
                return True
        return False