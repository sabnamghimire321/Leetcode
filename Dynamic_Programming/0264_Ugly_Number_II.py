import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        value = 1
     
        for _ in range(n):
            value = heapq.heappop(heap)
            for factor in (2, 3, 5):
                new_val = value * factor
                if new_val not in seen:
                    seen.add(new_val)
                    heapq.heappush(heap, new_val)
     
        return value
