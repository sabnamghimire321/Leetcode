from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        max_ending_here = nums[0]
        min_ending_here = nums[0]
        best = nums[0]

        for x in nums[1:]:
            candidates = (x, max_ending_here * x, min_ending_here * x)

            max_ending_here = max(candidates)
            min_ending_here = min(candidates)

            best = max(best, max_ending_here)

        return best
