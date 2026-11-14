class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # either 1 or 0 stones can remain
        # two heaviest sounds like a max heap
        # remember to add different back into the heap

        # bad solution: sorting an array at each step
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            x = maxheap[0]
            heapq.heappop(maxheap)
            y = maxheap[0]
            heapq.heappop(maxheap)
            # if not equal, we add the different back
            if x != y:
                heapq.heappush(maxheap, -abs(x-y))


        if len(maxheap) == 1:
            return -maxheap[0]
        return 0