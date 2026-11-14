import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        WE should track frequency and do the most popular ones first?

        But we don't want to resort every time we remove stuff. so we MUST use a heap or q

        n is the gap btw

        So we can only take n+1 at a time

        have a subarray n+1 that we take out of heap, then put back in afterwards?

        Is it costly to take stuff in a out of the heap so many times?
        '''
        curN = []
        heap = []
        count = 0
        freq = Counter(tasks)

        for t,c in freq.items():
            heapq.heappush(heap, (-c, t))   # neg for max heap
        
        while heap:
            # Count should increase by at most n+1 per cycle

            # Take the top N elements of heap, decrement their freq, and add them to N
            # Idles if heap is empty
            for i in range(n+1):
                if len(heap) != 0:
                    c,t = heapq.heappop(heap)
                    c += 1
                    if c != 0:
                        curN.append((c,t))
                count += 1
                if len(heap) == 0 and len(curN) == 0:
                    return count    # ends when everything had a freq of only 1 for the final turn (didnt get added to curN)
                # count += 1
                # print(f"Count={count}, round of n={i}")
            
            # Now we can add back on
            # print("Finished n+1 turns")
            # print(curN)
            while curN:
                c,t = curN.pop()
                heapq.heappush(heap, (c,t))
        #return count
        
        