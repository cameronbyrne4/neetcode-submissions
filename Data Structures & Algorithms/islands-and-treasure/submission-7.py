from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Multi source BFS
        - no helper func needed

        '''

        ROWS = len(grid)
        COLS = len(grid[0])
        v = set()
        queue = deque()

        # Function that adds cell to our queue if valid
        def bfs():
            dist = 0
            
            while queue:
                for _ in range(len(queue)): # Only this layer
                    r,c = queue.popleft()
                    grid[r][c] = min(dist, grid[r][c])  # don't update to be larger
                    dir = [(-1,0), (1,0), (0,-1), (0,1)]

                    for dr,dc in dir:
                        nr = r + dr
                        nc = c + dc # new coords to expand to IF valid

                        if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr,nc) in v or grid[nr][nc] == -1:
                            continue
                        else:
                            # Is valid
                            queue.append((nr,nc))
                            v.add((nr,nc))
                dist += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    v.add((r,c))
                    queue.append((r,c))
        
        bfs()
        
        
        return None

