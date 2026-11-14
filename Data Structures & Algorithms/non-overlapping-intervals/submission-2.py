class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # if they overlap... remove it! and add 1
        intervals.sort(key= lambda i : i[0])
        res = 0
        currEnd = intervals[0][1]

        for i in range(1,len(intervals)):
            # if it overlaps we fucking kill it
            if intervals[i][0] < currEnd: # same num is okay
                #effectively killing this one
                res += 1
                currEnd = min(currEnd, intervals[i][1])
                # ERROR: We have to think which one is more optimal to murder,
                # and that's whichever has the minimum currend
                
            else:
                currEnd = intervals[i][1]





        return res