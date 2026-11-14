class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Max heap based on frequency + Queue for cooldowns
        # The max heap doesn't care about what the letters actually are, it can be just frequencies
        # pop from heap, increase time
        # then add to queue with that new time +1, move from queue to heap
        self.time = 0
        # tasks must go into heap based on frequency...
        freq = collections.Counter(tasks).values()
        heap = [-x for x in freq]
        heapq.heapify(heap)
        
        q = deque()
        print(heap,q)
        while heap or q:
            self.time += 1
            
            if heap:
                curr = heapq.heappop(heap)
                if curr+1 < 0:
                    q.append((curr+1, self.time + n)) # (decreased freq, time until next ready)
            # check if anything on the queue can move back
            if q and q[0][1] == self.time:
                heapq.heappush(heap, q.popleft()[0])
                





        # queue has time of time + n
        return self.time