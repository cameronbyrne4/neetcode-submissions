class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        Can't sort

        Obviously can ignore any negative/zero values

        Duplicates do exist so can't sum..

        Answer must be at most n+1 mathematically, but still isnt O(1) enough

        So "aux" is the keyword we can use the existing nums array as we'd like

        IDEA:
        1. Pass 1 swap into proper positions
        2. See if i+1 == nums[i]
        '''

        for i in range(len(nums)):
            if nums[i] <= 0  or nums[i] > len(nums):
                continue
            # Put in proper spot sir
            
            # Swap if not in correct position
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]: # nums[i] needs to be swapped!
                j = nums[i]-1
                if nums[i] == nums[j]:
                    break   # case of duplicates
                nums[j], nums[i] = nums[i], nums[j]
                
            # Problem: when we send a number forwards and swaps with a bigger num, we forget it foreverrrrr
            # how about we only swap to go down?

        for i, n in enumerate(nums):
            if i+1 != n:         # Ex. nums[0] == 1
                return i+1        # Should be i+1 ideally
        return len(nums)+1