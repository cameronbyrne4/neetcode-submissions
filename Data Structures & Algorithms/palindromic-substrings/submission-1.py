class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Good, repeating logic! 
        Well, we should go through every single i:
            check every single palindrome expanding out from that point
            both even and odd sets
            if its a palindrome we add it! (if l ==r)
            # Pro tip: We can count the number of palindromes between r and l as r-l / 2
        '''    
        res = 0


        for i in range(len(s)):
            
            # Odd check
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Doesn't have to be longer, we sort of just add every palindrome to it
                # but it's a count so we don't even care what the substring looks like
                res += 1
                l -= 1
                r += 1
            # Even Check
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Doesn't have to be longer, we sort of just add every palindrome to it
                # but it's a count so we don't even care what the substring looks like
                res += 1
                l -= 1
                r += 1
        return res