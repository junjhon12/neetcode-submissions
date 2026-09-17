class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = sorted(nums)
        nums = set(nums)
        longest = 1

        for number in nums:
            if (number - 1) not in nums:
                length = 0
                while (number + length) in nums:
                    length += 1
                longest = max(length, longest)
        return longest

