class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        We would typically just sum the cost of every pair

        However we subtrack it for whenever points are on the same y = mx + b, subtracting the OVERLAP

        dict = { (m, b) -> [x1, x2, x3]}    can calculate the y already yk
        '''
        
        n = len(points)
        dists = [float('inf')] * n  # Distance from the MST
        v = set()
        total_cost = 0

        # End when we visit allnodes
        i = 0   # arbitrary node to begin with
        while len(v) < n:
            # Add to visited
            # Compute dists for all other points
            # Find the index of the minimum dist NOT visited
            # Add the minimum to total cost
            # shift i to the new one
            v.add(i)
            if len(v) >= n:
                break   # in case we are on the last node now
            min_idx, min_cost = 0, float('inf')
            for j in range(1,n):
                if j not in v:
                    dists[j] = min(dists[j], abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) )
                    if dists[j] < min_cost:
                        min_cost = dists[j]
                        min_idx = j
            
            total_cost += min_cost
            i = min_idx
        return total_cost

        # error some nodes are still inf
        # either dists[j] not updating or 

            
            
        

