class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        We are using greedy
        * not sorting by values

        * choosing between adding a number, or starting a new list with it

        * if curr is pos and the next num is pos, add it
        * if curr is neg, and the next num is pos, just take the next num instead
        * if curr is pos and the next num is neg
        * if curr is neg and the next num is neg, just take the next num instead lol
        '''
        res = nums[0]
        curr = 0
        for i in range(len(nums)):
            if curr < 0:
                curr = 0 # reset
            curr += nums[i]
            res = max(res, curr)

        return res
