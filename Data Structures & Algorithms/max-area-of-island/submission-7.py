from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        We can do BFS and increment a count by the len of q every iteration, reset for new q and compare to cur max

        Use 0 instead of visited
        '''

        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0  #visited
            res_area = 0           # area on this island

            while q:
                # only add if it's a valid square btw
                res_area += len(q)
                for _ in range(len(q)):
                    curR, curC = q.popleft()
                    

                    # append valid neighbors to q
                    for dr,dc in dirs:
                        nr = curR + dr
                        nc = curC + dc

                        if min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0: # if out of bounds or already been or water
                            continue
                        else:
                            grid[nr][nc] = 0
                            q.append((nr,nc))
            return res_area

        maxarea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxarea = max(maxarea, bfs(r,c))

        return maxarea
