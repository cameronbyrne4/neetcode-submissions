class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        Goal: find number of unique paths

        Note: grids with 1 are impassable and will always have a count of 0

        '''
        print("start")
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        grid = [[0 for _ in range(n)] for i in range(m)]

        # first col/row are just 1 unless they are blocked by an obstacle
        i = 0
        print("grid made")
        while i < m and obstacleGrid[i][0] == 0:
            grid[i][0] = 1
            i += 1
        
        i = 0
        while i < n and obstacleGrid[0][i] == 0:
            grid[0][i] = 1
            i += 1

        for r in range(1,m):
            for c in range(1,n):
                # if obstacle the value is just 0
                if obstacleGrid[r][c] == 1:
                    grid[r][c] = 0
                else:
                    above = grid[r-1][c]
                    left = grid[r][c-1]
                    grid[r][c] = above + left
                print(r,c)
        return grid[m-1][n-1]

