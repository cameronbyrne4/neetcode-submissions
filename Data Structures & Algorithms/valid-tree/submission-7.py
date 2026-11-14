class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Given an adj list for n nodes:
        Goal: Output true if valid tree

        Tree conditions:
            - all connected. Just make sure all are visited from our one run
            - no cycle

        Idea:
            - run DFS once
        '''

        adj = [[] for _ in range(n)]
        visit = [0] * n
        
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i, prev):
            visit[i] = 1

            for nei in adj[i]:
                # Bad if visited and not prev
                if visit[nei] == 0:
                    if dfs(nei,i):
                        return True 
                elif nei != prev:   # visited and not prev condition
                    return True

        visit[0] = 1
        cycle = dfs(0,-1)
        if cycle:
            return False

        # If we are here, no cycles were detected, just need to make sure all are visited
        # No values can be 0
        return True if min(visit) == 1 else False

