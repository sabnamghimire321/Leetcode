class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (target + total) % 2 != 0 or abs(target) > total:
            return 0
        subset_target = (target + total) // 2
        
        dp = [0] * (subset_target + 1)
        dp[0] = 1
        
        for num in nums:
            for c in range(subset_target, num - 1, -1):
                dp[c] += dp[c - num]
                
        return dp[subset_target]
