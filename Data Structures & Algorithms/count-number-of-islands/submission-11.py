class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        1 IS LAND, 0 IS WATER
        FIND THE NUMBER OF ISLANDSSSS
        WE COULD KEEP A VISITED ARRAY OR JUST CHANGE SHIT TO 0 FLOOD IT WITH WATERRRR
        '''

        res = 0

        def dfs(r,c):
            # BASE CASE OUT OF BOUNDS OF ON WATER
            if r < 0 or c < 0 or r > len(grid)-1 or c > len(grid[0])-1 or grid[r][c] == "0":
                return

            # Other case nga
            grid[r][c] = '0'
            dfs(r-1 ,c )
            dfs(r+1 ,c )
            dfs(r ,c-1 )
            dfs(r ,c+1 )

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r,c) # goal is to flood the island so it can't be re discovered
                    res += 1
        return res