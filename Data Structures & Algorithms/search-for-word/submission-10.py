class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Start on the first letter obviously

        Tracking coordinates we have already used in visited (x,y)

        requirements for exploring new cells in 4 directions
        - within overall bounds
        - follows the next letter
        - is not in the visited set
        '''
        def bt(r,c,i,visit):
            if i == len(word)-1: # we made it to the end
                self.valid = True
                return
            # if we aren't there yet, we are at the right one, so just add to valid
            # Can save incrementing index for the bt call
            #visit.add()
            # Iterate over every directions
            dirs = [[-1,0], [1,0], [0,-1], [0,1]]
            for d in dirs:
                dr = r + d[0]
                dc = c + d[1]
                if (0 <= dr < ROWS) and (0 <= dc < COLS) and ((dr,dc) not in visit) and board[dr][dc] == word[i+1]:
                    visit.add((r,c))
                    bt(dr,dc,i+1, visit)
                    visit.remove((r,c))

        ROWS = len(board)
        COLS = len(board[0])

        self.valid = False
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == word[0]):
                    visit = set()
                    visit.add((r,c))
                    bt(r,c,0,visit)
        return self.valid