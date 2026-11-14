class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # starts off sorted
        # there are some different cases
        #1: in between, chill insert 
        '''
        Start could be within a current interval:
            if end is within, we just return the original list
            if end is outside, we check with the next interval (WHILE)
                If it's before the start of the next interval:
                    we extend the first intervals end to there
                if it's inside the next interval:
                    we extend the first interval end to the end of this interval and delete this interval
        '''
        # add stuff, find the start, then find the end, then add stuff
        n = len(intervals)
        i = 0
        res = []

        #new interval hasnt started yet
        while i<n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # currently new ints start is in the frame
        # go until the end is less than th e curr's start
        while i<n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i += 1
        res.append(newInterval)
        while i<n:
            res.append(intervals[i])
            i += 1
        return res

            
