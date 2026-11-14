class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # unvisited grid nodes start a new component
        # Count how many new searches i have
        # use either dfs or bfs to reach all of them

        # SET: hash map but only the keys
            # .add and .remove in O(1) and can do "if node in visited" in O(1)
        
        # We could also just check the adjacent to 1 to see if they are not visited, then count ++

        def dfs(row,col):
            # base case out of bound
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            
            # base case not connected
            if grid[row][col] == "0":
                return

            # base case explored
            if (row,col) in visited:
                return

            # main case --> add to visited and proceed to check neighbords
            # Inbounds, 1, and unvisited
            visited.add((row,col))
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)


        visited = set()
        count = 0
        # rows
        for i in range(len(grid)):
            # cols
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    count +=1
                    dfs(i,j)
                    
                    # commence bfs or dfs to mark everything in it as visited

        return count