class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        Fill up the graph
        - probably need to do some DFS
        - No cycles allowed

        WE TRYNA TOPO SORT
        1. build the adjacency list
        2. we have a set for visited overall, and a set for cycles
        '''
        res = []
        visited = set()
        cycle = set()

        # Make an adjacency list
        graph = {i: [] for i in range(numCourses)}     # no inclusive
        for a,b in prerequisites:
            graph[a].append(b)           # key: course, val: [prerequisites]

        # Write our backbone function
        def dfs(i):
            # Case: we have seen this number in our current DFS run
            if i in cycle:
                return False

            # Case: we have seen this number from some other run (can skip since we've done it)
            if i in visited:
                return True
            
            cycle.add(i)
            # Loop over the children
            for prereq in graph[i]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(i)

            visited.add(i)
            res.append(i)
            return True 

        # Run the DfS
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res