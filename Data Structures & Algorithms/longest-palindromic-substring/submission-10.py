class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        use each boy as the center
        '''
        
        residx =0
        reslen = 0
        for i in range(0,len(s)): # for every single fucking index

            # Set pointers
            # for even paly's only extend to the left!
            r = i
            l = i

            # Odd check
            while l >= 0 and r <= len(s)-1 and s[l]==s[r]:
                if (r-l+1) > reslen:
                    residx = l
                    reslen = r-l+1
                l = l-1
                r = r+1
            
            # Even check
            l= i
            r = i+1

            while l >= 0 and r <= len(s)-1 and s[l]==s[r]:
                if (r-l+1) > reslen:
                    residx = l
                    reslen = r-l+1
                l = l-1
                r = r+1

            

            
        return s[residx: residx+reslen]