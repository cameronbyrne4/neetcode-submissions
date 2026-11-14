class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Start of sequence is on numbers who are not one larger than others


        '''

        g = set()
        for n in nums:
            g.add(n)

        starters = []
        for n in nums:
            if n-1 not in g:
                starters.append(n)

        res = 0
        streak = 1
        for s in starters:
            i = s
            while i+1 in g:
                streak += 1
                i += 1

            res = max(streak,res)
            streak=1

        return res