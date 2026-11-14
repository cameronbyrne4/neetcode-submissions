import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        Goal: find the min cost path, where cost is the largest number in the path
        '''

        n = len(grid)   # nxn grid
        heap = []
        processed = set()
        costs = [[float('inf')] * n for _ in range(n)]
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        costs[0][0] = grid[0][0]
        heapq.heappush(heap, (costs[0][0], (0,0)))

        while heap:
            cost, (r,c) = heapq.heappop(heap)

            # We need to check processed because maybe a path with high cost can be added to heap many times as cost updates
            if (r,c) in processed:
                continue
            processed.add((r,c))

            for dr, dc in dirs:
                nr,nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nc >= n or nr >= n or (nr,nc) in processed:
                    continue
                costs[nr][nc] = min(costs[nr][nc], max(grid[nr][nc], cost))
                heapq.heappush(heap, (costs[nr][nc], (nr,nc)))



        return costs[n-1][n-1]

