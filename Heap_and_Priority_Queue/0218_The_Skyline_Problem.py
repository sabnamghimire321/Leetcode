import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []

        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()

        heap = [(0, float('inf'))]
        result = []
        prev_height = 0

        i = 0

        while i < len(events):
            x = events[i][0]

            while i < len(events) and events[i][0] == x:
                _, neg_height, right = events[i]

                if neg_height != 0:
                    heapq.heappush(heap, (neg_height, right))

                i += 1

            while heap[0][1] <= x:
                heapq.heappop(heap)

            current_height = -heap[0][0]

            if current_height != prev_height:
                result.append([x, current_height])
                prev_height = current_height

        return result
