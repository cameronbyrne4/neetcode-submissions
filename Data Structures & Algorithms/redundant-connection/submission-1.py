class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        Starts off as an MST btw 

        Go thru the list of edges

        See if a can reach b. if so, we have two paths and it can be removed... ok

        new visited set each time via popping
        '''
        visit = set()
        adj = [[] for _ in range(len(edges)+1)]   # n edges currently

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(start_node, node, goal_node):
            if node == goal_node:
                return True
            
            visit.add(node)
            for nei in adj[node]:   # must exclude goal_node if we are at start_node
                if node == start_node and nei == goal_node:
                    continue
                if nei not in visit:
                    if dfs(start_node, nei,goal_node):
                        return True

            visit.remove(node)
            return False

        res = []
        for a,b in edges:
            # We have to remove the direct edge before we run it btw
            visit.clear()
            if dfs(a,a,b):
                res = [a,b]
        return res