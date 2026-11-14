class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Notes:
        - we can replace up to k chars with whatever we want
        - return len of longest consecutive substring

        Idea:
        - Is there a smart way to approach this?
        - I believe we target the char that has the lowest count to begin with
        - XXXX: should be replacing things WITH the most requent char

        Here's how we use sliding window:
        - expand window until we replace k different ones
        - then shift to the next k, shrinking and expanding the window
        '''

        # MONKEY APE CODE YEAH
        # NEW TECH: dict.get(), and dict.values()

        # freqs and globals
        count = {}
        res = 0
        l = 0
        maxfreq = 0

        # R GOES THRU S
        for r in range(len(s)):
            # Increment count of current char by 1. CANNOT DO +=1 OR IT ERRORS
            count[s[r]]  = 1 + count.get(s[r],0)
            maxfreq = max(maxfreq, count[s[r]])
            
            # Make the window valid before we can compare to res
            # Make sure the number of things changed is at most k
            # if it's out of range, we have to move the left fella
            while (r-l+1) - maxfreq > k:
                # Move the left, and it doesn't exist in subarray any more
                count[s[l]] -= 1
                l += 1

            # Update result with maybe the size of the window (if the window is valid)
            res = max(res, r-l+1)

        return res











