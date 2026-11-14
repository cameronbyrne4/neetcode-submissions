
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        DP problem or backtracking
        Goal: # of distinct ways to climb to top of staircase

        dp[i] refers to number of ways to get to that stair, like a counter
        '''
        memo = defaultdict()
        memo = {1: 1, 2: 2}

        def dp(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = dp(n-1) + dp(n-2)
                return memo[n]


        return dp(n)