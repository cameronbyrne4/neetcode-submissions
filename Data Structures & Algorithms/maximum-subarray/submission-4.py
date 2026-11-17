class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        If the sum is neg forget about it, the next number will always be larger
        '''
        res = nums[0]
        s = nums[0]
        for n in nums[1:]:
            s += n
            res = max(res,s,n)
            if s < 0:
                s = 0

        return res