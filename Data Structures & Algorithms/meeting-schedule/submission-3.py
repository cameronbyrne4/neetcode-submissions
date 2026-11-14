"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort
        intervals.sort(key = lambda element : element.start) # let each elem
        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True
# Shit solution is every single interval time slot put down and checking if any of them
# put down in the same space... O(n*m) where m is the length of interval

# O(nlogn) suggests i should sort by the first one