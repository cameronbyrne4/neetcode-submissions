class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        We literally did this on an exam man, lock in
        '''
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n            # dp[i] is the max money we can have at a house
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2,n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[n-1]
