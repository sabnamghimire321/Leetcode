from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [None] * n

        for start in range(n):
            if color[start] is not None:
                continue

            color[start] = 0
            queue = deque([start])

            while queue:
                node = queue.popleft()

                for nxt in graph[node]:
                    if color[nxt] is None:
                        color[nxt] = 1 - color[node]
                        queue.append(nxt)
                    elif color[nxt] == color[node]:
                        return False

        return True
