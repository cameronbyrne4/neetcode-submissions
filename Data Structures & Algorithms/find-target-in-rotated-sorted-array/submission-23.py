class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        INPUT: originally sorted array thats now rotated.
            items are unique
        OUTPUT: return index of a target

        EX. 5,6,1,2,3,4 (2 rotate)
        ex. 2,3,4,5,6,1 (5 rotate)
        =======
        SIMPLE BINARY SEARCH. WHERE IS THE PIVOT?
        IF m<r, the right is in order and the pivot is on the left
        IF l < m, the left is in order and the pivot is on the riht
        BASICALLY WHENEVER IN ORDER WE CAN TREAT AS A RANGE

        '''
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target: #THIS IS THE GOAL WE WANT TO CENTER IN ON THE TARGET
                return m
            
            # otherwise...
            if nums[l] <= nums[m]:  # LEFT SIDE IS IN ORDER, PIVOT IS ON THE RIGHT
                # go left if its in the range!!
                if nums[l] <= target < nums[m]:
                    r = m-1
                    
                else:   # IF TARGET NOT IN THE RANGE WE GO RIGHT
                    l = m+1
                    
            else:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1

        return -1