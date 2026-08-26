from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_ending_here = nums[0]
        best_overall = nums[0]

        for x in nums[1:]:
            best_ending_here = max(x, best_ending_here + x)
            
            best_overall = max(best_overall, best_ending_here)

        return best_overall
