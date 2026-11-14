class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        - right down left up
        '''
        rowMax = len(matrix)
        colMax = len(matrix[0])
        rowMin, colMin = 0, 0
        result  = []

        # iterate in a circle
        while rowMin < rowMax and colMin < colMax:
            # right iterations
            for i in range(colMin, colMax):             # This gets the ENTIRE top row
                result.append(matrix[rowMin][i])
            rowMin += 1
            # down
            for i in range(rowMin, rowMax):
                result.append(matrix[i][colMax-1])
            colMax -= 1
            # left
            if rowMin >= rowMax or colMin >= colMax:
                break
            for i in range(colMax-1, colMin-1, -1):
                result.append(matrix[rowMax-1][i])
            rowMax -= 1
            # up
            for i in range(rowMax-1, rowMin-1, -1):
                result.append(matrix[i][colMin])
            colMin += 1
            

        return result