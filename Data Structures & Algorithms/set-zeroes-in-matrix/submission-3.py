class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        use the first row/col as our marker for if everything shoudl be 0

        second go thru it
        '''
        ROWS = len(matrix)
        COLS = len(matrix[0])
        row1_0 = False
        col1_0 = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                    if r == 0:
                        row1_0 = True
                    if c == 0:
                        col1_0 = True

        # second pass, starting with rows? or nah just look
        for r in range(ROWS-1,0,-1):
            for c in range(COLS-1,0,-1):    # doesnt have to be backwards lol
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if row1_0 == True:  # fill row 1 with 0
            for c in range(COLS):
                matrix[0][c] = 0
        if col1_0 == True:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        return None

        