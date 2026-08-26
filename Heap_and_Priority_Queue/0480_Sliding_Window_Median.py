import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = []
        large = []
        delayed = set()
        side = {}
        small_size = 0
        large_size = 0
        result = []

        def prune_small():
            while small:
                index = small[0][1]
                if index in delayed:
                    heapq.heappop(small)
                    delayed.remove(index)
                else:
                    break

        def prune_large():
            while large:
                index = large[0][1]
                if index in delayed:
                    heapq.heappop(large)
                    delayed.remove(index)
                else:
                    break

        def rebalance():
            nonlocal small_size, large_size
            while small_size > large_size + 1:
                prune_small()
                value, index = heapq.heappop(small)
                heapq.heappush(large, (-value, index))
                side[index] = 1
                small_size -= 1
                large_size += 1

            while large_size > small_size:
                prune_large()
                value, index = heapq.heappop(large)
                heapq.heappush(small, (-value, index))
                side[index] = 0
                large_size -= 1
                small_size += 1

        for i, num in enumerate(nums):
            if not small or num <= -small[0][0]:
                heapq.heappush(small, (-num, i))
                side[i] = 0
                small_size += 1
            else:
                heapq.heappush(large, (num, i))
                side[i] = 1
                large_size += 1

            if i >= k:
                old_index = i - k
                delayed.add(old_index)
                if side[old_index] == 0:
                    small_size -= 1
                else:
                    large_size -= 1

            rebalance()
            prune_small()
            prune_large()

            if i >= k - 1:
                if k % 2 == 1:
                    result.append(float(-small[0][0]))
                else:
                    result.append((-small[0][0] + large[0][0]) / 2.0)

        return result
