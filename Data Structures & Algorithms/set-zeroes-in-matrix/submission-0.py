class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        instead of updating the whole thing right away we keep a list for x and y that need to be zeroed
        '''
        zeroR = set()
        zeroC = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeroR.add(r)
                    zeroC.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in zeroR or c in zeroC:
                    matrix[r][c] = 0


        