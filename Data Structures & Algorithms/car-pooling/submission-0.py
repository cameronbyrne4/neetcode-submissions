class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        Need separate arrays for starts and ends type SHIT

        Or heaps?? nah just sort each array
        '''
        starts = []
        ends = []
        for p,s,e in trips:
            starts.append([s,p])
            ends.append([e,p])
        
        starts.sort()
        ends.sort()

        l,r,a = 0,0, len(trips)

        # try to traverse thru all
        num_passengers = 0
        while l < len(trips):
            if starts[l][0]  < ends[r][0]:
                # starts is first, so we add to curnum
                num_passengers += starts[l][1]
                l += 1
                if num_passengers > capacity:
                    return False
            else:
                num_passengers -= ends[r][1]
                r += 1

        return True

