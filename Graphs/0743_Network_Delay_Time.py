import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n+1)}

        for u, v, w in times:
            adj[u].append((v, w))

        dist = {i: float("inf") for i in range(1, n+1)}
        dist[k] = 0

        heap = [(0, k)]

        while heap:
            d, node = heapq.heappop(heap)

            if d > dist[node]:
                continue

            for nxt, w in adj[node]:
                nd = d + w

                if nd < dist[nxt]:
                    dist[nxt] = nd
                    heapq.heappush(heap, (nd, nxt))

        worst = max(dist.values())

        return worst if worst != float("inf") else -1
