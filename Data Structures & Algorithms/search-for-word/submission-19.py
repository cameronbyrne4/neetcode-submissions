class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        grid dfs

        multi source?

        index to track what letter we are on

        return any()
        '''
        self.output = False
        ROWS, COLS = len(board), len(board[0])
        

        def dfs(r,c,i,v):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in v or board[r][c] != word[i]:
                return
            
            # By now we are in bounds and on the correct letter!
            v.add((r,c))
            i += 1
            if i == len(word):
                self.output = True  # we made it!
                return
            else:
                dir = [(-1,0), (1,0), (0,-1), (0,1)]

                for dr, dc in dir:
                    nr = r + dr
                    nc = c + dc
                    dfs(nr, nc, i,v)
            v.remove((r,c))




        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    v = set()
                    dfs(r,c,0,v)
        return self.output
