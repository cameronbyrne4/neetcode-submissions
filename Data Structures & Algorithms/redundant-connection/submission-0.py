class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        input: list of undirected edges in a connected tree
        output: [a,b] where we can remove the edge but still be connected / non-cyclical

        Use disjoint union find algo (partial implementation works for this)
        '''

        N = len(edges)
        parent = [i for i in range(N+1)]            # each node's parent is themselves at the start
        rank = [1] * (N+1)                          # size of each cc

        # Find's the parent of n (Recursive)
        def find(n):
            if n != parent[n]:      
                parent[n] = find(parent[n])
            return parent[n]

        # True if they are not already connected
        def union(u1,u2):
            # Find parents:
            p1,p2 = find(u1), find(u2)
            if p1 == p2:
                return False

            # Union by rank
            if rank[p1] > rank[p2]:
                parent[p2] = p1             # p2 is a child of p1
                rank[p1] += rank[p2]        # adjust rank
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for a,b in edges:
            if not union(a,b):          # If this connection has already been connected previously...
                return [a,b]