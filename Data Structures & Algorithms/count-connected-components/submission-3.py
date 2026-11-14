class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        Notes:
        - undirected
        - input: array of undirected edges
        - output: int count of CC's

        -- decrease component count when a node is connected to a tree that it isnt ALREADY IN
        '''
        graph = {i: [] for i in range(n)}
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        res = 0         # Start with n connected components when it's just nodes
        visited = set()
        cc = set()

        def dfs(i, parent):
            # if graph[i]
            if i in visited:
                return
            
            visited.add(i)
            
            for neighbor in graph[i]:
                if neighbor != parent:
                    dfs(neighbor, i)
            
    
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                res += 1
        
        return res


        