class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for index, value in enumerate(nums):
            if (target - value) in nums[index + 1:]:
                return [index, nums.index((target - value), index+1)]
