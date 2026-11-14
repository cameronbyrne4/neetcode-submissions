class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        Backtrack
        - either include it in the set or not
        - we can do an isPalindrome helper check at the very end?
        - actually, we can cut off branches in the **Case 2, start new substr** if the old one isnt a palinddrmoe
        '''
        # chars = list(s) # tbh we can probably skip this one...
        result = []
        part = [] # ['a', 'aa', 'b']
        def validPalindrome(s, l ,r) -> bool: # input is my current mini list
            
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True

        # i = index of char in s, sub = sublist, list = bigger list (not as big as result)
        def backtrack(i):
            # end condition
            if i >= len(s):
                result.append(part.copy())

            # loop over other indexes
            for j in range(i, len(s)):
                if validPalindrome(s, i, j):    # Segment of s from index i to index x
                    part.append(s[i:j+1])       # Add the valid segment to the running list
                    backtrack(j+1)              # Move on to the next string
                    part.pop()
        backtrack(0)
        return result

