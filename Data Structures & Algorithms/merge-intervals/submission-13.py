class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()    # should sort by the start times?

        '''
        - Choosing when to add intervals to an output array
        - If the next interval starts before current is ended:
            - We extend current to the max(end current, end next)
            - Then we repeat by looking at the next interval
        '''
        output = []

        cs = intervals[0][0]
        ce = intervals[0][1]
        for i in intervals[1:]:
            if i[0] > ce:
                # no overlap --> add output and reset interval
                output.append([cs,ce])
                cs,ce = i[0],i[1]
                
            else:
                ce = max(ce, i[1])
                
    
        # append whatever we have at the very end
        output.append([cs,ce])
        return output
