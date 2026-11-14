from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        * Cannot sort
        Can convert to a set then look to see if in it?

        value of the set is how many additional characters after it are covered

        return max of the dict
        '''
        if not nums:
            return  0
        count = defaultdict(int)
        for n in nums:
            count[n] = 1
        
        for n in nums:
            #print(count)
            if n not in count:  # already deleted it and processed it
                continue
            if count[n] == 1:   # uninvestigated so far
                i = n+1
                while (i) in count: # effectively a dfs
                    count[n] += (count[i])
                    del count[i]
                    i += 1
        
        return max(count.values())