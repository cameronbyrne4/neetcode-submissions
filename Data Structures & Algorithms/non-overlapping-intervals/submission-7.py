class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Greedyish.

        For each overlap, one has to go. it makes sense that it should be the one that ends later
        '''
        intervals.sort()
        removed = 0
        #curstart = intervals[0][0]
        curend = intervals[0][1]

        for s, e in intervals[1:]:
            #print(f"s={s}, e={e}, curned={curend}")
            if s < curend:
                # overlap detected, one must go
                removed += 1
                # no need to change start because we are going in order
                curend = min(e, curend)
                continue
            curend = e # always moveed





        return removed