class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        '''
        Choosing 4 numbers that maximize produc
        '''
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])