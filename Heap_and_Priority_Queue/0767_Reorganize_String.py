import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [(-c, ch) for ch, c in counts.items()]
        heapq.heapify(heap)
        result = []
        
        while len(heap) >= 2:
            c1, ch1 = heapq.heappop(heap)
            c2, ch2 = heapq.heappop(heap)
            result.extend([ch1, ch2])
            if c1 + 1 < 0:
                heapq.heappush(heap, (c1 + 1, ch1))
            if c2 + 1 < 0:
                heapq.heappush(heap, (c2 + 1, ch2))
        
        if heap:
            c, ch = heapq.heappop(heap)
            if -c > 1:
                return ""
            result.append(ch)
            
        return "".join(result)
