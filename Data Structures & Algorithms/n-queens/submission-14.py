class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        We can do backtracking or some sort of pruning? There are going to be a lot of solutions:
            * Don't want to check at the very end because then thered be like O(n!) different boards to check
            * Check as we go, as to only place in valid places
            * if no valid place exists, we do not append and we break here 
        
        How to determine if a new placement is valid?
            * i iterates over the rows (one row at a time from row 1..n)
            * Must not be in a used column (can store a set of length n?)
            * Must not be in diagonals?? ()

            Sums of diagonals

            0   1   2
            1   2   3
            2   3   4

            Different of diagonals (abs val)

            0   1   2
            1   0   1
            2   1   0

            Ok so we can have 2 sets to store each direction of diagonals?

        '''
        cols = set()
        diag1 = set()
        diag2 = set()
        coord = [-1] * n
        out = []

        def bt(r):
             
            if r == n:  # done, append solution board to output
                board = []
                for x in coord:
                    row = ["."] * n
                    row[x] = "Q"
                    board.append(''.join(row))

                out.append(board)
                return

            # iterate on the next row/coord only if checks are clear for the next
                # Add to necessary checks and remove from checks before and after the run

            # we can check over all columns other than c, then r+1 if we end up finding a valid one?
            #print(r)
            for col in range(n):
                #print(coord)
                #print(f"Check r,col={r,col}")
                
                
                # perform checks
                if (col not in cols) and ((col + r) not in diag1) and ((col-r) not in diag2):
                    # add them, then run, then remove
                    cols.add(col)
                    diag1.add(col+r)
                    diag2.add(col-r)
                    coord[r] = col
                    bt(r+1)

                    cols.remove(col)
                    diag1.remove(col+r)
                    diag2.remove(col-r)
                    coord[r] = -1
            return


        # start it off on every 
        bt(0)
        return out