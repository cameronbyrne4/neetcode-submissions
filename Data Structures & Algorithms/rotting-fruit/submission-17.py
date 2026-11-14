from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        multi source bfs
        '''
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque() 
        dir = ((0,1), (0,-1), (1,0), (-1, 0))
        
        
        # first run to scope rottens
        grid_max = grid[0][0]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2: # Rotting
                    q.append((r,c))
                grid_max = max(grid_max, grid[r][c])
        
        if grid_max == 0:
            return 0
        elif grid_max == 1:
            return -1
        
        # BFS TIME
        time = 0
        while q:
            # increment time at end
            for _ in range(len(q)):
                # Turn fresh --> rotten
                r,c = q.popleft()

                # scope out next moves that are VALID only
                for dr,dc in dir:
                    nr = r + dr
                    nc = c + dc

                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
            if q:
                time += 1
        
        # Final check to make sure no fresh fruit are isolated
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: # Rotting
                    return -1

                    print("failed")
        print(q)
        return time