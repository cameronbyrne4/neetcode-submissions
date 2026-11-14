class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        do a dfs
        look for first letter and go letter by letter
        keep a visite
        false if we never make it
        '''
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r,c,idx, visited):
            
            # if we are out of bounds OR if we are the wrong fucking letter OR visited, cancel
            if r < 0 or r >= ROWS or c<0 or c>=COLS or board[r][c] != word[idx] or (r,c) in visited:
                return False
            print("checking: ", board[r][c], "| idx and len is ", idx, " - ", len(word))
            # success we made it to the last letterrrr
            if idx == len(word)-1:
                print("over")
                return True

            visited.add((r,c))

            # else we still have more to go
            res= dfs(r-1,c,idx+1, visited) or dfs(r+1,c,idx+1, visited) or dfs(r,c-1,idx+1, visited) or dfs(r,c+1,idx+1, visited)
            visited.remove((r,c))
            return res
        for i in range(ROWS):
            for j in range(COLS):
                visited = set()
                if dfs(i,j,0, visited): # starts off by checking if its the start of the word
                    return True
        return False