class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        2dp memoization
        return 1 when we reach the trophy
        return 0 if we are out of bounds
        we can go both right and down


        '''
        
        memo = {}
        
        def dp(i,j):
            if i== m-1 and j == n-1:
                return 1
            if i==m or j == n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]

            # I'm not going to do conditions since I chcked already?
            nextPaths=0
            if i != m-1:
                nextPaths += dp(i+1,j)
            if j != n-1:
                nextPaths += dp(i,j+1)
            memo[(i,j)] = nextPaths
            return nextPaths

        return dp(0,0)          # aka number of paths from 0,0