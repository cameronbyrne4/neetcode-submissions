class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        can have 3 pointers. swap 0 to the front and 2 to the back at each i

        can only move on from i if it's no longer swappable
            - swapping would just be the same value 
        """
        n = len(nums)
        l,r = 0, n-1

        # march l and r to be the next spot for stuff
        while l < n and nums[l] == 0:
            l += 1
        while r >= 0 and nums[r] == 2:
            r -= 1
        i = l

        def swap(a,b) -> None:
            print("swapping index:", a,b)
            nums[a],nums[b] = nums[b], nums[a]

        while  i <= r:
            if nums[i] == 1:
                i += 1
                
            elif nums[i] == 0:
                # swap it to l,
                # Then move l to where it needs to be
                # We don't know whats at nums[i] now but can wait for the next iteration
                swap(i,l)
                l += 1
                i += 1
            elif nums[i] == 2:
                swap(i,r)
                r -= 1
            

            # If 0, swaps to l and l moves
            # if 2, swaps with r and r moves
            # Stops when nums[i] == 1, then increment i
            # Other stop conditions: 
            
        


        return nums