class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        Conditions:
        - # strs that s1 and s2 are broken into is either 0 or 1 len apart
        - They must do the alternating shit

        IDEA: Two pointers on s1 and s2
        While pointers not at end
            just alternate to the other pointer if we can't recognize it
            if we can't recognize BOTH then there's a problem
        at the end check if the number of swaps is 1 off
            ^^ or like we can't even get to the end if it isn't, right?

        Can we assume s3 consists of letters from s1 and s2
        ALSO what happens if both s1 and s2 have the same character at the index
        Then we would need to continue the one we are on?
        Example:
            s1 = aaba
            s2 = accc
            s3 = 

        SOLUTION: 2dp and memoization
        '''
        # dp represents a coordinate grid for the two strings
        # let s1 be rows
        # s2 be cols
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}                 # (x,y) = bool

        def dfs(i,j):
            # Base case 1 and 2
            if i == len(s1) and j == len(s2):
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            
            # Two success cases
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                # we just confirmed i was in range, matches, and now moving past
                return True
            
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True

            # no matches!
            dp[(i,j)] = False       # Cache as false to prevent future efforts
            return False

        # Final run
        return dfs(0,0)


