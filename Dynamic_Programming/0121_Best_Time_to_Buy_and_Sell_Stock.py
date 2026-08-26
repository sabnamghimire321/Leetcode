from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        min_so_far = prices[0]
        best = 0

        for price in prices[1:]:
            best = max(best, price - min_so_far)
            min_so_far = min(min_so_far, price)

        return best
