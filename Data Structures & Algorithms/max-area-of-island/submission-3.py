class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r,c) -> int:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r,c) in visited:
                return 0

            visited.add((r,c))
            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)

        maxArea = 0
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited: # new one
                    islandArea = dfs(i,j)
                    maxArea = max(maxArea, islandArea)

        return maxArea