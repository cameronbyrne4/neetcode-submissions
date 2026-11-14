class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        Bad way:
        -- each square:
        ---- check if can flow to either

        Good Way:
        -- at each square list the coords it can reach!
        -- do this for squares on the borders
        -- add to two different lists
        -- check if any coords are shared in each list
        
        '''
        ROWS = len(heights)
        COLS = len(heights[0])
        result = []
        pacific = set()
        atlantic = set()

        def dfs(r,c,ocean):
            # Error case of grid!
            if (r,c) in ocean or r < 0 or c < 0 or r == ROWS or c == COLS:
                return
            # Normal case: add to ocean and keep chugging
            ocean.add((r,c))
            # Go in all 4 directions!
            # Only if the height is equal or MORE... and obviously if it's in the damn grid
            heightCur = heights[r][c]
            if 0 <= r-1 < ROWS and heightCur <= heights[r-1][c]:
                dfs(r-1,c,ocean)
            if 0 <= r+1 < ROWS and heightCur <= heights[r+1][c]:
                dfs(r+1,c,ocean)
            if 0 <= c-1 < COLS and heightCur <= heights[r][c-1]:
                dfs(r,c-1,ocean)
            if 0 <= c+1 < COLS and heightCur <= heights[r][c+1]:
                dfs(r,c+1,ocean)
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dfs(r,c,pacific)
                if r == ROWS-1 or c == COLS-1:
                    dfs(r,c,atlantic)

        #compare the 2 sets to append things to result
        print(pacific)
        print(atlantic)
        for peak in pacific:
            if peak in atlantic:
                result.append(peak)
        
        return result
        
