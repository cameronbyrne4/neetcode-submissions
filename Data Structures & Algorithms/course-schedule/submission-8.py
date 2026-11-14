class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Breaks if:
        1. cyclic
        
        detected by managing two sets!
        '''
        n = len(prerequisites)
        adj = [[] for _ in range(numCourses)]
        visit = set()

        for a,b in prerequisites:
            adj[a].append(b)    # b --> a
                                # {a: [prerequisites of a]}

        def dfs(node, cur_path_set):
            # check failures now rather than after
            if node in cur_path_set:
                # Cycle detected
                return False

            if node in visit:
                # Already proven to not be cyclic, dont worry about it
                return True
            # mark visited
            cur_path_set.add(node)

            for nei in adj[node]:
                if not dfs(nei, cur_path_set):
                    return False

            # Clean up:
            cur_path_set.remove(node)
            # add to visit after safe dfs
            visit.add(node)
            return True
        
        # Run dfs over everything
        
        for i in range(numCourses):
            if i not in visit:  # Saving time
                
                res = dfs(i, set())  # starts a new path set
                if not res:
                    return False
        
        # Never returned False
        return True
