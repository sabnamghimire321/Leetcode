from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        full_mask = (1 << n) - 1
        queue = deque()
        visited = set()
        
        for i in range(n):
            state = (i, 1 << i)
            queue.append((i, 1 << i, 0))
            visited.add(state)
     
        while queue:
            node, mask, dist = queue.popleft()
            if mask == full_mask:
                return dist
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                state = (neighbor, new_mask)
                if state not in visited:
                    visited.add(state)
                    queue.append((neighbor, new_mask, dist + 1))
                    
        return 0
