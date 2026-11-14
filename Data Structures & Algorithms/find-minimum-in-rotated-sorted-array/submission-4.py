class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Important to draw this one out! took me a long time back in the day

        Must use binary search

        ex [123456]

        low spin (lowest in left side) [561234]
        if m < r that's in order!!
            if l < m:
                its in order, return l
            else
        hi spin (lowest in right side) [345612]


        So the condition to branch is ???
        '''

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            print("Vals are: ", nums[l], nums[m], nums[r])
            # case 0 all sides in order (rotate 0 or n times)
            if nums[l] < nums[m] < nums[r]:
                return nums[l]
            # case 1 right side in order (rotated less than halfway around)
            elif nums[m] < nums[r]:
                r = m # Note: not doing m-1 for reasons
                print(" Go left")
            
            # case 2 left side in order (rotated over halfway around)
            else:
                l = m+1
                print("go right")
        
        return nums[r]
        

        