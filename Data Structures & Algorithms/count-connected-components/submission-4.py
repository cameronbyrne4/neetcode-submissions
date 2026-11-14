class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        Simply do dfs and incrment 1 whenever we have a new island
        '''
        visit = set()
        adj = [[] for _ in range(n)]

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            # just dont explore anything in visited that's not a neighbor
            visit.add(node)

            # no work to do or to return bools or anything
            # work on neighbors
            for nei in adj[node]:
                # Dont explore visited
                if nei not in visit:
                    dfs(nei)
        
        num_cc = 0
        for i in range(n):
            if i not in visit:
                num_cc += 1
                dfs(i)

        return num_cc