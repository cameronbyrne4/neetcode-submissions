class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        invalid if in set or not digit on not 1-9

        Must check all rows
            check all cols
            check all boxes
        '''
        checker = set(range(1,10))   # check if vals in here
        cur9 = set()    # checks for dupes

        # ROWS
        for i in range(9):
            cur9.clear()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if int(board[i][j]) not in checker or int(board[i][j]) in cur9:
                    return False
                cur9.add(int(board[i][j]))

        # COLS
        for i in range(9):
            cur9.clear()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if int(board[j][i]) not in checker or int(board[j][i]) in cur9:
                    return False
                cur9.add(int(board[j][i]))

        # SQUARES

        for i in range(0,9,3):
            for j in range(0,9,3):  
                cur9.clear()
                # get all in either direction
                for a in range(3):
                    for b in range(3):
                        if board[i+a][j+b] == ".":
                            continue
                        if int(board[i+a][j+b]) not in checker or int(board[i+a][j+b]) in cur9:
                            return False
                        cur9.add(int(board[i+a][j+b]))



        return True