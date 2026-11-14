import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        dijkstras and return the min dist, unless dist is inf then return -1
        '''
        adj = [[] for _ in range(n+1)]
        dists = [float('inf')] * (n+1)
        processed = [0] * (n+1)
        heap = []

        for a,b,w in times:
            
            adj[a].append((b,w))

        # initialize starter
        dists[k] = 0
        heapq.heappush(heap, (0,k))

        # Begin dijkstras
        while heap:
            dist, node = heapq.heappop(heap)

            if processed[node]:
                continue
            
            processed[node] = 1

            for neighbor, weight in adj[node]:
                # If we decrease distance we can add it to the heap
                new_distance = dists[node] + weight
                if new_distance < dists[neighbor]:
                    dists[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))
        
        # Final search
        print(dists)
        m = max(dists[1:])
        print(m)
        return -1 if m == float('inf') else m

