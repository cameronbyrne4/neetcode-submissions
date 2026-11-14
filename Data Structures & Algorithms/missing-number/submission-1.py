class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        no sort sadly O(1) space
        '''
        n = sum(nums)

        # expected - actual = missing
        # 123456 = 21
        return (((len(nums)+1)*len(nums))//2) - n