import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        fuel = startFuel
        stops = 0
        i = 0
        n = len(stations)
     
        while fuel < target:
            while i < n and stations[i][0] <= fuel:
                heapq.heappush(heap, -stations[i][1])
                i += 1
            if not heap:
                return -1
            fuel += -heapq.heappop(heap)
            stops += 1
     
        return stops
