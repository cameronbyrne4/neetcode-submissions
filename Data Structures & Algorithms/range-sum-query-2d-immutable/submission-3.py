class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        # prefix sums on each row + the value above them (unless row 0)
        
        for r in range(len(matrix)):
            prefix = 0
            for c in range(len(matrix[0])):
                prefix += matrix[r][c]
                curval = prefix
                if r != 0:  # add square above if not on first row
                    curval += self.matrix[r-1][c]
                print(r,c)
                self.matrix[r][c] = curval
        print(self.matrix)
        # points store the sum that is up and to the left of them?

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        # Add bottom right, sub 1 above top right, sub 1 left of bot right
        # add  outside of top left corner twice
        total += self.matrix[row2][col2]
        if col1 != 0:
            total -= self.matrix[row2][col1-1]
        if row1 != 0:
            total -= self.matrix[row1-1][col2]
        if col1 != 0 and row1 != 0:
            total += self.matrix[row1-1][col1-1]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)