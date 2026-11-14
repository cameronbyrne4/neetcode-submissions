class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        nxn is good we can move the 4 "corners" shifted for i


        
        '''
        n  = len(matrix)
        l, r = 0, n-1
        while l < r:
            for i in range(r-l):
                top, bottom = l, r
                #temp for the top left
                tempval = matrix[top][l+i] 
                #bl to tl (override top left since stored on temp)
                matrix[top][l+i] = matrix[bottom-i][l]
                # br to bl
                matrix[bottom-i][l] = matrix[bottom][r-i]
                # tr to br
                matrix[bottom][r-i] = matrix[top+i][r]
                # tl to tr uring temp
                matrix[top+i][r] = tempval
                # shrink matrix
            l += 1
            r -= 1

            

