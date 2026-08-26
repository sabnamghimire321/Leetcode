import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        by_capital = sorted(zip(capital, profits))
        affordable = []
        i = 0
        n = len(profits)
 
        for _ in range(k):
            while i < n and by_capital[i][0] <= w:
                heapq.heappush(affordable, -by_capital[i][1])
                i += 1
            if not affordable:
                break
            w += -heapq.heappop(affordable)
 
        return w
