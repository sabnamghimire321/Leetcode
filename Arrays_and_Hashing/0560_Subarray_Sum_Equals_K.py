from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        running_sum = 0
        count = 0

        for x in nums:
            running_sum += x
            count += prefix_count.get(running_sum - k, 0)
            prefix_count[running_sum] = prefix_count.get(running_sum, 0) + 1

        return count
