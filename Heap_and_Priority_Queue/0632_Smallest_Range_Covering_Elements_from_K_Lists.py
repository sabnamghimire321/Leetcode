import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(lst[0], i, 0) for i, lst in enumerate(nums)]
        heapq.heapify(heap)
        current_max = max(lst[0] for lst in nums)
        best = (heap[0][0], current_max)
 
        while True:
            val, i, j = heapq.heappop(heap)
            if current_max - val < best[1] - best[0]:
                best = (val, current_max)
            if j + 1 == len(nums[i]):
                break
            next_val = nums[i][j + 1]
            current_max = max(current_max, next_val)
            heapq.heappush(heap, (next_val, i, j + 1))
 
        return list(best)
