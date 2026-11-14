class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        -- input: string of digits
        -- output: number of ways to decode it
        -- can only be broken into numbers 1-26, anything else is not valid

        Some constraints:
        - Can take single numbers if it's 1-9. Have to stop if 3-9. if it's zero we are fucked
        - Can take the next number if current number is 1 and next is 0-9, or current is 2 and next is 0-6
        - 

        Used recursion sol, but switching to memoization
        '''
        memo = {}
        def dp(i):
            
            if i in memo: # Case: we made it all the way
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            # Almost solved it but forgot this step
            addedPaths = dp(i+1)       # Always adds the next one
            # Only add the second one conditionally
            if i < len(s)-1:
                if (s[i] == '1') or (s[i] == '2' and s[i+1] <= '6'):
                    addedPaths += dp(i+2)
            memo[i] = addedPaths
            return addedPaths

        return dp(0)

