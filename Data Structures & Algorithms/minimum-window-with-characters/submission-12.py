class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if m > n or m == 0:
            return ""


        '''
        Ideas:
        * make a freq array for t and try to match it? Well not match but include for the relevant numbers in t to be less than whats in s

        * Should be constant since we are using a 26 length array, unrelated to length of t

        * Expand r while < n until it's valid, then shrink l until its NOT.
            Once it's invalid after moving l, we compare the max length values, can append a substring of s using the pointers to our output
        '''
        l,r = 0,0
        cur_len = 0
        min_len = float('inf')
        min_idx = 0 # update to l
        output = "" # change each time max len updates

        t_freqs = [0] * 52
        s_freqs = [0] * 52

        def index(c: str) -> int:
            # Returns array index of a character
            if c.isupper():
                idx = ord(c)-ord('A')+26
            else:
                idx = ord(c)-ord('a')
            return idx

        for c in t:
            t_freqs[index(c)] += 1
        
        def isInside(s_arr, t_arr) -> bool:
            # helper checks if t freqs is inside of the s arr
            for i in range(52):
                if t_arr[i] > s_arr[i]:
                    return False
            return True

        for r in range(n):  # iterates overss
            s_freqs[index(s[r])] += 1
            cur_len += 1
            
            # If success, we need to shrink l until it no work

            while l <= r and isInside(s_freqs, t_freqs):
                #
                s_freqs[index(s[l])] -= 1
                l += 1
                cur_len -= 1
            
                if cur_len + 1 < min_len:
                    #print("New curlen: ", cur_len+1)
                    min_len = cur_len+1
                    min_idx = r+1
                    
        if min_len == float('inf'):
            return ""
            
        output = s[min_idx-min_len: min_idx]
        return output




        