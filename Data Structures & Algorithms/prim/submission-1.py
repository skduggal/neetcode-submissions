import heapq
from typing import List

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        min_heap = [(0,0)]
        total_weight = 0

        while min_heap and len(visited) < n:
            w, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            
            visited.add(node)
            total_weight += w

            for nei, weight in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (weight, nei))

        return total_weight if len(visited) == n else -1