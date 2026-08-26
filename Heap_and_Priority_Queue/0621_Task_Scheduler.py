import heapq
from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-c for c in counts.values()]
        heapq.heapify(heap)
        time = 0
 
        while heap:
            batch = []
            for _ in range(n + 1):
                if heap:
                    batch.append(heapq.heappop(heap))
            for count in batch:
                if count + 1 < 0:
                    heapq.heappush(heap, count + 1)
            time += len(batch) if not heap else n + 1
 
        return time
