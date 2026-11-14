class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        We can do a sliding window with two pointers

        length is r - l + 1

        iterate over right becase we have to add 1 by one eventually

        If r is in the set: let l catch up and remove everything otw:

        then update max

        keep a set at all times
        '''
        freq = set()
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1

        maxlen = float('-inf')
        l = 0
        for r in range(n):
            # Catchup l until not in set
            while s[r] in freq:
                freq.remove(s[l])
                l += 1
            # now we can add
            freq.add(s[r])
            maxlen = max(maxlen, r-l+1)



        return maxlen
