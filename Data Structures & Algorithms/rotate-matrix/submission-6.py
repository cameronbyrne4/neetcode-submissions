class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        Topic: Math
        Goal: rotate clockwise 90 degrees

        0,0 -> 0,1 -> 1,1 -> 1,0 -> 0,0
        0,2 -> 2,6
        new r = old c
        new c = n - old r
        0 1 2 3 4 5
        0 1 * 3 4 5
        0 1 2 3 * 5
        0 * 2 3 4 5
        0 1 2 * 4 5
        0 1 2 3 4 5
        '''
        n = len(matrix)

        for i in range(0,n//2):
            for j in range(i, n-i-1):
                r,c = i, j
                temp = matrix[r][c] # save for last rotations

                # 4 rotations
                for _ in range(3):
                    matrix[r][c] = matrix[n-c-1][r]
                    r,c = n-c-1, r
                    
                matrix[r][c] = temp

        return None