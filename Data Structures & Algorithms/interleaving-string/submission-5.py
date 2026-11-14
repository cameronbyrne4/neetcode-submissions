class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        About same number of substrings

        Substrings go one after another boom boom boom (should be iterable or pointers because it goes in the original roder for each substr)

        Easy conditions --> s1 + s2 = s3 length
                        --> same frequency counter
                        NOT NOT NECESSARILY, since order matters

        2 Dp solution:
            - dp[i] = can we get to index i of s3?
                or is the number of substr? with -1 if impoassible

                return dp[m-1[n-1]]

            a b c c a
        b   1 1 0 0 0   0
        c   0 1         0
        b   0           0
            0 0 0 0 0   ?
        Forming: abbcccba

        - T if above or left is T (the previous pos on s3) AND one of the curr pointersd match, we are ok?
        dp[i][j] means that s3[:i+j] is solvable using s1[:i] and s2[:j]
        - First case: 
        '''

        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # dp[i][j] means we can form interleaving string up to that point on s3[i+j]

        
        dp[0][0] = 1    # It's possible to form "" using "" and ""
        
        
        for r in range(m+1):
            for c in range(n+1):
                above, left = 0, 0
                # has above:
                if r != 0 and dp[r-1][c] == 1:
                    above = 1
                # has left
                if c != 0 and dp[r][c-1] == 1:
                    left = 1

                s1_match, s2_match = 0, 0
                if r != 0 and s1[r-1] == s3[r+c-1]:
                    s1_match = 1
                if c != 0 and s2[c-1] == s3[r+c-1]:
                    s2_match = 1
                if (above and s1_match) or (left and s2_match):
                    dp[r][c] = 1

        return bool(dp[-1][-1])
