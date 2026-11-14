class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        -- create a directed graph from the prereqs as ajacency lists
        -- do DFS on each connected component to see if there are repeats (visited)
        '''
        graph = {i: [] for i in range(numCourses)}
         # each key --> list of neighbors it points to
        for a,b in prerequisites:           # b --> a
            
            graph[b].append(a)

        visited = set()

        def dfs(course): # returns true if there is no cycle
            # cycle case
            if course in visited:
                return False

            # no kids case breaks the cycle
            
            # normal case
            visited.add(course)

            # iterate on the children
            for c in graph[course]:
                # IF ANY KIDS ARE FUCKED, ITS FALSE
                if not dfs(c):
                    return False
            visited.remove(course)
            
            return True
            # reset them
        # Trying to take courses 0 thru n
        n = numCourses
        for i in range(n):
            if not dfs(i):
                return False # cycle detected
        return True
