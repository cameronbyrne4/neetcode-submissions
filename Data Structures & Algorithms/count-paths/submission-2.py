class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        This is math?
        you can only move down or right

        0 0 0 0
        0 0 0 0
        0 0 0 0
        0 0 0 0

        each points is the sum of left + above grids
        '''
        paths = defaultdict(int)        # (r,c) --> ways

        for i in range(m):
            paths[(i,0)] = 1
        for i in range(1,n):
            paths[(0,i)] = 1

        # Don't need dp can just go left to right lol

        for i in range(1,m):
            for j in range(1,n):
                paths[(i,j)] = paths[(i-1, j)] + paths[(i, j-1)]
        
        return paths[(m-1, n-1)]