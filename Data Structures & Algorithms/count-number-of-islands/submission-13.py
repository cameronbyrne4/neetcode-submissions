class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Just run dfs and every time we run it island goes up by 1

        Gotta make sure to not start dfs on visited land, either mark with # or in a visited set
        '''
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        def dfs(r,c):
            # check coords
            # check visited via #
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
                return
            if grid[r][c] != "1":
                return
            
            # real actions hell year
            grid[r][c] = "#"
            dir = [(0,1), (0,-1), (-1,0), (1,0)]

            for dr,dc in dir:
                nr = r + dr
                nc = c + dc
                dfs(nr,nc)  # purpose is to mark them down
            
            # on another problem we did post processing to like remove from visited, that was when we had multi source i believe


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r,c)
                    res += 1
        return res