class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        2dp

        min(top path, left path)

        first col and row must be the prefix sums, no variability there

        '''
        m = len(grid)
        n = len(grid[0])

        # for i in range(1,n):
        #     grid[0][i] += grid[0][i-1]

        # for i in range(1,m):
        #     grid[i][0] += grid[i-1][0]

        for i in range(m):
            for j in range(n):
                above = float('inf')
                left = float('inf')
                if i == 0 and j == 0:
                    continue
                if i != 0:
                    above = grid[i-1][j]
                if j != 0:
                    left = grid[i][j-1]
                grid[i][j] += min(above,left)  # choosing which direction to path from
                # If not first row, can compare the one above it
                # if not first col, can compare the one left of it
        
        print(grid)
        return grid[m-1][n-1]