class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        We know how to find the min element. do we just go in a circle?

        ((imagine finding 4 or 2))
        1: not sort
        123456
        ELIF 2: under half
        612345
        ELSE 3: over half
        345612


        Strat:
        any side that is sorted AND target within bounds: we can do a normal binary search

        '''
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                    return m
            if nums[l] < nums[m] < nums[r]:
                # Binary search on just this portion (guaranteed to return)
                # l,r already set
                while l <= r:
                    m = (l+r)//2
                    if nums[m] == target:
                        return m
                    elif target > nums[m]:
                        l = m+1
                    else:
                        # target small
                        r = m-1
            elif nums[m] < nums[r]:
                if nums[m] <= target <= nums[r]:
                    # Binary search in the right portion
                    l = m
                    while l <= r:
                        m = (l+r)//2
                        if nums[m] == target:
                            return m
                        elif target > nums[m]:
                            l = m+1
                        else:
                            # target small
                            r = m-1
                else:                       # Ex 612345 and looking for 6,1, or 2
                    # Shift to left side!
                    r = m-1
            else:       # Left side is sorted
                if nums[l] <= target <= nums[m]:
                    # Binary search in the right portion
                    r = m
                    while l <= r:
                        m = (l+r)//2
                        if nums[m] == target:
                            return m
                        elif target > nums[m]:
                            l = m+1
                        else:
                            # target small
                            r = m-1
                else:                       # Ex 612345 and looking for 6,1, or 2
                    # Shift to right side
                    l = m+1
        return -1




