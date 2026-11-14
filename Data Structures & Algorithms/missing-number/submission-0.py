class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Sum trick
        '''
        expected = 0
        for i in range(len(nums)+1):
            expected += i

        actual = 0
        for i in range(len(nums)):
            actual += nums[i]

        return expected - actual