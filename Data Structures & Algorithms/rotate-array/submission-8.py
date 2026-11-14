from collections import defaultdict
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        This solutions is bad for memory tho...

        Better solution:
        - reverse the whole ass array 
        - then again reverse the two halves
        """
        if k%len(nums) == 0:
            return nums
        # reverse whole ting
        l ,r = 0, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        # reverse the two halves. second half starts with index==k
        l,r = 0, (k%len(nums))-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Second half
        l,r = k%len(nums), len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        return nums

        