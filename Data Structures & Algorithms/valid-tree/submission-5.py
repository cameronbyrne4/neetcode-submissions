class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Loop over edges list to create a graph
        run DFS on each node to ensure it hits all nodes without cycling (visited)
        return true if we can get thru them add

        '''
        visited = set()
        # Goal of this dfs is to put everything we can reach into visited w/o cycles
        def dfs(curr, parent):
            # Base case and default logic
            if curr in visited:
                return False
            visited.add(curr)

            # recursive step
            for edge in graph[curr]:
                if edge != parent and not dfs(edge, curr):
                    return False
                
            return True

        graph = defaultdict(list)
        for a,b in edges:       # undirected btw
            graph[a].append(b)
            graph[b].append(a)      # keep track of parent so this isnt fucked

        # We only need one traversal because if it works, it will reach all nodes
        if dfs(0,-1) and len(visited) == n:
            return True
        else:
            return False

        
        