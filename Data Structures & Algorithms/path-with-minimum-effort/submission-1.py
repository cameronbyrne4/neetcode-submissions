import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
        Goal: Find min effort traversal = smallest difference between any two consecutive cells in the traversal

        Could do some sort of DFS or dp?

        lets try dijkstras
        - no adj
        - dist array is 2d
        - processed set

        '''
        ROWS, COLS = len(heights), len(heights[0])
        heap = []
        processed = set()
        efforts = [[float('inf') for i in range(len(heights[0]))] for _ in range(len(heights))]  # what to start at?
        efforts[0][0] = 0
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]

        heapq.heappush(heap, (0, (0,0)))

        while heap:
            e, (r,c) = heapq.heappop(heap)
            if (r,c) in processed:
                continue
            processed.add((r,c))

            for dr,dc in dirs:
                nr,nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr,nc) in processed:
                    continue
                efforts[nr][nc] = min(efforts[nr][nc], max(e, abs(heights[r][c]-heights[nr][nc]))) # e == efforts[r][c]
                heapq.heappush(heap,(efforts[nr][nc], (nr,nc)))

        
        return efforts[ROWS-1][COLS-1]