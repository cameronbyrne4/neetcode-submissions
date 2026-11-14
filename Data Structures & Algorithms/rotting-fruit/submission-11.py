class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        -- Run bfs on all the rotten fruit
        -- every level is ++ to a count
        -- Find the maximum count
        -- at the end, return -1 if there are any fresh fruit (1) left in the

        New strat:
        -- Add the rottens to the queue as our starting points

        -- for items in the queue:
            
            add all the valid neighbors to the queue
        increment result by 1 after all the children are ran
        '''
        ROWS = len(grid)
        COLS = len(grid[0])
        result = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    # result = max(result, minutes)

        while q:
            numRotters = len(q)
            for i in range(numRotters):
                r,c = q.popleft()
                
                # add valid children to the q
                dirs = [[r-1,c], [r+1,c], [r,c-1], [r,c+1]]
                for dr,dc in dirs:
                    if 0<=dr<ROWS and 0<=dc<COLS and grid[dr][dc] == 1:
                        # better to make rotten here
                        grid[dr][dc] =  2
                        q.append((dr,dc))
            if q:
                result += 1



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return result
