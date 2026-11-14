class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        We have to binary search it wtf?

        Odd length -> move to side thats not the same

        
        '''
        l,r = 0, len(nums)-1


        while l < r:
            m = (l+r) // 2

            # make m to it's even side
            if m%2 == 1:
                m -=1

            # pairs are ok -> go right
            if nums[m] == nums[m+1]:
                l = m+2
            
            else:
                r = m
        return nums[l]
            
