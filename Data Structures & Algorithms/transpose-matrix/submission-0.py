class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        main diagonal and bottom triangle dont need any work

        nvm bro its not always a fucking square omg
        '''

        ROWS = len(matrix)
        COLS = len(matrix[0])

        out = [[0 for _ in range(ROWS)] for _ in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS):
                out[c][r] = matrix[r][c]
        return out    