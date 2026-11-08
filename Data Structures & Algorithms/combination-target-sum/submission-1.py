class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        nums.sort()

        for num in nums:
            for t in range(num, target + 1):
                for combo in dp[t - num]:
                    dp[t].append(combo + [num])
        return dp[target]