from collections import defaultdict
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
        # machines to run n processes
        Answer: maximum that are overlapping

        can make 2 ds storing the start and end times
        '''
        starts = Counter([x.start for x in intervals])
        ends = Counter([x.end for x in intervals])
        if intervals == []:
            return 0
        start = min(starts.keys())
        end = max(ends.keys())

        maxrooms = float('-inf')
        currooms = 0
        for i in range(start, end+1):
            if i in starts:
                currooms += starts[i]
            if i in ends:
                currooms -= ends[i]
            maxrooms = max(maxrooms, currooms)
        return maxrooms

        