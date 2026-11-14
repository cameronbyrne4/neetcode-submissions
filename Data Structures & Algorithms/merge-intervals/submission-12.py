class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        For ones with the same start:
            They all take the maximum ending time

        We keep expanding the end for any starts that are within that end
        
        When we find starts that are OUTSIDE of the current end range,
            res append the very first start + variable ending
            reset start and end to the next guy
        '''
        intervals.sort()
        res = []
        curstart = intervals[0][0]
        curend = intervals[0][1]

        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            print("current i's start end:, ", start, end)
        
            # Ending case no conflict:
            if start > curend:
                res.append([curstart,curend])
                curstart = start
                curend = end
                print("startend cur: ", curstart, curend)
            
            # Other case conflicts
            else:
                print('conflict')
                curend = max(curend, end)


            # Case: next interval overlaps with the cur one someone
        res.append([curstart,curend])
        return res

