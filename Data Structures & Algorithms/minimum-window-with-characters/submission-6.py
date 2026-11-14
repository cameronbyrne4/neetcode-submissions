class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Variable window size,
        returning a string

        How to check if all characters are within a string:
            See if every element in the array is less than the other

        Move thru r:
            substr = s[l:r] or something
            update hash
            if the hash contains the other hash:
                move left until it doesnt
                if str len is less than result:
                    update result = str
        '''
        # Helper function checks if f2 freq array is inside of f1's
        def contains(f1, f2) -> bool:
            # f1 must always have higher counts 
            for i in range(52):
                if f1[i] < f2[i]:
                    return False
            return True

        if len(t) > len(s):
            return ''
        
        result = s  # start off super big so size can decrease with min()
        freq_t = [0] * 52
        for c in t:
            # Lower and upper both matter
            if 'a' <= c <= 'z':
                freq_t[ord(c) - ord('a')] += 1
            else:
                freq_t[ord(c) - ord('A') + 26] += 1

        freq_cur = [0] * 52
        l = 0
        self.foundsolution = False
        for i in range(len(s)):
            c = s[i]

            # Update freq cur
            if 'a' <= c <= 'z':
                freq_cur[ord(c) - ord('a')] += 1
            else:
                freq_cur[ord(c) - ord('A') + 26] += 1

            # Branch if it contains the str
            if contains(freq_cur, freq_t):
                self.foundsolution = True
                while l < len(s) and contains(freq_cur, freq_t):
                    # Move L until no longer contains
                    c = s[l]
                    # Update freq cur
                    if 'a' <= c <= 'z':
                        freq_cur[ord(c) - ord('a')] -= 1
                    else:
                        freq_cur[ord(c) - ord('A') + 26] -= 1
                    l += 1
                    # L is now at a point where we DO NOT contain!
                # Update res
                curstr = s[l-1:i+1]
                if len(curstr) < len(result):
                    result = curstr
            
        if self.foundsolution:
            return result
        else:
            return ""
