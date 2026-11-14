class Solution:
    def numSquares(self, n: int) -> int:
        '''
        dp up to n

        each one we take the minimum number of steps to get there,
        try over every square

        '''
        dp = [n] * (n+1)        # Max it could take is with just 1's
        dp[0] = 0                # 1 step to the first squares

        for i in range(1, n+1):
            for j in range(1, i+1): # can go up to i size
                sq = j * j
                if i - sq < 0:
                    break
                    # sq got too big
                dp[i] = min(dp[i], 1 + dp[i - sq])


        return dp[-1]
