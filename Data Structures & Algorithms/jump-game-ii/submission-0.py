class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Jump 1 = greedy can you do it?
        Jump 2 = dp min at idx

        - We can jump up. bottom up only works, not top down?
        '''
        n = len(nums)
        dp = [float('inf')] * n   # dp[i] = min jumps to get to i-th index
                                # 0 to n-1
        dp[0] = 0

        for i in range(n):
            # Every spot in jumping range is potentially updated?
            for j in range(nums[i]+1):
                if i+j < n:
                    dp[i+j] = min(dp[i+j], dp[i] + 1)

        return dp[n-1]
