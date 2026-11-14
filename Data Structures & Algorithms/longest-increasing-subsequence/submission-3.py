class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        isnt this dp?
        we either remove or do not remove a char, and say what is the longets subsequence at that point

        N^2 space suggests we gotta do 2d what the FUCK? 
        I think we can just go forward and if its not increasing we go backwards?
        '''

        dp = [1] * len(nums)    # dp[i] = longest LIS we can form using up to nums[i] inclusive

        for i in range(1, len(nums)):
            # have to go back until it IS smaller
            j = i-1
            while j >= 0:
                if nums[j] < nums[i]:   # valid increase, continue to grow
                    # logic
                    dp[i] = max(dp[i], dp[j] + 1)
                j -= 1
                        



        #print(dp)
        return max(dp)