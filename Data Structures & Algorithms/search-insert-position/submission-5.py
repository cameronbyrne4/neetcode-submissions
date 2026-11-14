class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Just do bin search

        1 2 4 5 6 8 9

        3 --> at l, which was above r? 7?
        '''
        n = len(nums)
        l,r = 0, n-1

        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            else:
                if nums[m] > target:    #go left
                    r = m-1
                else:
                    l = m+1
        print(l,r)
        return l