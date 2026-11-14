class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Thinks abt greedy
        1. remove ones with move conflicts
        2. remove largest ones X
        3. Remove whatever conflicts X
            -------------
               -  -   - -  
               would remove 4 instead of 1

        Solution:
         1. go thru and if we have an overlap we remove the one that ENDS latest

        Overlap condition: start before the curEnd (overlap is okay)

        End goal is a counter where the freq at each number is at most 1 (no overlap)
        '''

        res = 0
        intervals.sort()
        curend = float('-inf')

        for i in range(len(intervals)):
            # No Overlap resets curned
            # Overlap increments res and compared curend
            if intervals[i][0] >= curend:       # Safe!
                curend = intervals[i][1]
            else:                               # Conflict merge
                res += 1
                curend = min(curend, intervals[i][1])



        return res