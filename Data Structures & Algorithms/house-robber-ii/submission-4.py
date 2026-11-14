class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        can't rob both first and last in the same run
        Solution: run on (1,n) and on (0,n-1)
        '''
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[1], nums[0])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        # reset 1 array after saving the max value
        # Run on front subarray ( exclude last val)
        for i in range(2,n-1):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        max1 = dp[-2]
        
        print("First val: ", max1, "\n")

        dp = [0] * n
        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])
        # Back subarray (exclude first val)
        for i in range(2,n-1):
            dp[i] = max(dp[i-2] + nums[i+1], dp[i-1])
        max2 = dp[-2]
        print("Second val: ", max2, "\n")
        return max(max1,max2)