class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        -- maintain a set for currently visited in the dfs
        -- if we hit a border, everything remains as is
        -- if we go thru the whole island without reaching a border island,
            -- everything in visited turns into an x

        Hint: only run dfs from all the border squares and add that to a big list
        '''
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        def dfs(r,c):
            # Edge case
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or board[r][c] == "X":
                return
            
            # Default
        
            visited.add((r,c))

            # run in all 4 directions
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        # run on all the border
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
        
        # mark all 'O' not in visited with an 'X'
        print(visited)
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited:
                    board[r][c] = "X"

