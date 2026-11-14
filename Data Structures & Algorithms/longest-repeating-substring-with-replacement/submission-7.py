class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        XXXYYYYYXXX

        zyxyxyz

        I know to replace one with lowest freq

        To make them ALL the same make everythijg the highest freq char
        (does least replacements)

        do a sliding window containing the max number of replacements we can

        len is length of window
        '''

        res = 0
        maxlen = float("-inf")

        unique = set(s)

        # use each char as the base
        for u in unique:
            # do a sliding window with two pointers, tracking the count of this character
            countU = 0
            l = 0 
            for r in range(len(s)):
                if s[r] == u:
                    countU += 1
                # catch up window size with number to be replaced
                # # of non "u" chars can only replace k of them
                while ((r-l+1) - countU) > k:
                    if s[l] == u:
                        countU -= 1
                    l += 1

                # Once the size is finalized we can compare max
                maxlen = max(maxlen, (r-l+1))
        
        return maxlen



        
