class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for index, value in enumerate(nums):
            sub_sum = (target - value)
            if sub_sum in nums[index + 1:]:
                return [index, nums.index(sub_sum, index+1)]
