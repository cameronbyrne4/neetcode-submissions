class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Sorting too slow

        Can we do sum then div by 2?

        bit xor against eachother, because two of the same number xorred == 0
        '''
        bit = nums[0]

        for n in nums[1:]:
            bit ^= n
        
        return bit