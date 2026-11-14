import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        '''
        Oh my god im not even marching through a string. s doesnt exist

        do a 3 elemtn max heap and us the most frequent one.

        When should we use it twice in a row tho?22222
        '''
        res = []
        heap = []   # max heap
        if a != 0:
            heapq.heappush(heap, (-a, "a"))
        if b != 0:
            heapq.heappush(heap, (-b, "b"))
        if c != 0:
            heapq.heappush(heap, (-c, "c"))
        sideline = []   # for triplet that had to wait

        # do most popular except for if it results in 3 in a row. can just check backwards on res I guess insetad of using more space

        while heap:
        
            count, car = heapq.heappop(heap)
            if len(res) >= 2 and res[-1] == res[-2] == car:
                # if triplet, just sideline for now
                sideline = [count, car]
                if not heap:
                    return ''.join(res)
                
                # and add the next most (guaranteed to not be triple)
                count, car = heapq.heappop(heap)
            res.append(car)
            if count+1 < 0: # only add if we arent done yet
                heapq.heappush(heap, (count+1, car))

            # re add sideline before moving on
            if len(sideline) > 0:
                res.append(sideline[1])
                if sideline[0] + 1  < 0:
                    heapq.heappush(heap, (sideline[0]+1, sideline[1]))
                sideline = []

        return ''.join(res)