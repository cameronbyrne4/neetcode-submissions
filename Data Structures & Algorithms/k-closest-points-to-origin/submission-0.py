class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # could store 3 values (x,y,dist) in a min heap
        # or we can convert to distance?
        points_dist = []
        for p in points:
            x,y = p[0],p[1]

       
        points_dist = [(math.sqrt(p[0]**2 + p[1]**2),p) for p in points]
        heapq.heapify(points_dist)

        res = []
        for i in range(k):
            res.append(points_dist[0][1]) # takes the coords out the tuple
            heapq.heappop(points_dist)
        return res
        
        