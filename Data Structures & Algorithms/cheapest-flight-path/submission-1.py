class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        Need array to count number of stops --> NO THIS WONT WORKKK
        bellman ford is the way
        '''

        dists = [float('inf')] * n
        dists[src] = 0
        # k stops means that we can go to k+1 iterations?
        for _ in range(k+1):
            # use all edges to try to update dists
            news = [dists[i] for i in range(n)]
            
            for a,b,x in flights:
                if dists[a] != float('inf'):
                    news[b] = min(news[b], dists[a] + x)
                
                # problem need to be only updating once per turn
            dists = [news[i] for i in range(n)]
        
        return dists[dst] if dists[dst] != float('inf') else -1