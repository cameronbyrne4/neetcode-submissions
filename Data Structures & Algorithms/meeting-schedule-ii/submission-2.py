"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        go one by one adding to a result list
        *if it doesn't fit in one row, put it on the next, over and over
        '''
        count = 0
        starts = []
        ends = []
        for ints in intervals:
            starts.append(ints.start)
            ends.append(ints.end)
        starts.sort()
        ends.sort()

        s = 0 # index on the start val array
        e = 0
        n = len(intervals)
        res = 0
        
        while s<n and e<n:
            # Add up how many happening until the first end time
            if starts[s] < ends[e]:
                s+=1
                count += 1
                res = max(res,count)
            else:
                e += 1
                count -= 1
        return res
        