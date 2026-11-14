import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        # counter heap?? max heap
        '''
        if 6:
            cannot be 4
        if 7:
             can be 4, cannot be 5
        '''
        counts = Counter(s)
        if max(counts.values()) > ((len(s)+1)//2):
            return ""
        heap = []
        res = []
        
        for c,n in counts.items():
            heapq.heappush(heap, (-n,c))    # max heap of the counts

        while heap:
            n, c = heapq.heappop(heap)
            print("n,c: ", n, c)
            if not res or (res and c != res[-1]):
                res.append(c)   # we can only append if its not current on top dupe
                if n+1 < 0:
                    heapq.heappush(heap, (n+1, c))
            elif heap:
                m,b = heapq.heappop(heap)
                print("     m,b: ", m , b)
                res.append(b)
                if m + 1 < 0:
                    heapq.heappush(heap, (m+1,b))
                res.append(c)   # we can only append if its not current on top dupe
                if n+1 < 0:
                    heapq.heappush(heap, (n+1, c))
        return ''.join(res)
            