from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Increasing order
        Don't change relative orders
        remove duplicates so each element is either 0,1,2 count

        move in place
        '''
    
        n = len(nums)
        if n < 3:
            return n

        read,write = 2, 2   # 2 pointers we run with
        
        while read != n:
            if nums[read] == nums[write-2]:
                # dupe found, do not write it
                read += 1
                
            else:
                # not a dupe, keep writing
                nums[write] = nums[read]
                read += 1
                write += 1

        return write  #good