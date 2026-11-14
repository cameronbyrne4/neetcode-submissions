class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # at each chest, do bfs updating with min(current min length, length from chest + 1)

        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r,c):
            visited = set()
            queue = deque([(r,c)])
            visited.add((r,c))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            # loop through all available from this chest
            while queue:
            # TODO: bfs logic
                # pop left (current coords)
                # make sure they're clean
                # if they are, 
                    #add to visited
                    # update counts
                    # loop on the rest of em
                a, b = queue.popleft()
                visited.add((a,b))
                for dr, dc in directions:
                    # Cross out: out of bounds, water or treasure, or visited
                    if (a+dr < 0 or a+dr >= ROWS or b+dc < 0 or b+dc >= COLS 
                    or grid[a+dr][b+dc] == 0 or grid[a+dr][b+dc] == -1
                    or (a+dr,b+dc) in visited):
                        continue
                    else:
                        # Add to queue so we can keep expanding
                        queue.append((a+dr,b+dc))
                        
                        # Update distance at that point
                        grid[a+dr][b+dc]  = min(grid[a+dr][b+dc], grid[a][b]+1)

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    bfs(i,j)
        # no return :)
        