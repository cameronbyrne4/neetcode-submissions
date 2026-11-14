from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Window size is fixed to be len(s1)

        Track freq of the window
        +1 and -1 whenever we move it
        if it matches we are happy asf jiggla

        1. add the first len s1 into freq
        2. then move the window along

        r-l +1 = len(s1)
        So to begin with when l = 0 --> r = len(s1)-1
        And as we move, l = r + 1 - len(s1)
        '''
        if len(s1) > len(s2):
            return False

        freq_s1 = [0] * 26
        freq_window = [0] * 26

        # Set up freq_s1
        for s in s1:
            freq_s1[ord(s)-ord('a')] += 1
        
        l = 1-len(s1)       # starts negative which is chill, just dont use if below 0
        for r in range(len(s2)):
            # Add the one at r to window
            freq_window[ord(s2[r])-ord('a')] += 1
            # remove the one before l to window (since l is included in window)
            if l > 0:
                freq_window[ord(s2[l-1])-ord('a')] -= 1
            l += 1
            if freq_s1 == freq_window:
                return True
            print(freq_window)
        # iterate over all
        #End case
        return False
