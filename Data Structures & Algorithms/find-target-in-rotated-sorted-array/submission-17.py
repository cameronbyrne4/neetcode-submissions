class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        PROBLEM UNDERSTANDING:
        -- using binary search to find the index of number
        -- array is a simple 1,2,3,...,n


      int l = 0;
        int r = nums.size()-1;

        while (l <= r) {
            int m = (l+r)/2;
            if (nums[l] <= nums[m] && nums[m] <= nums[r]) {
                return nums[l];
            } else if (nums[m] <= nums[r]) {
                r = m; // no -1
            } else if (nums[l] <= nums[m]) {
                l = m+1;
            }
        }
        return -1;
        '''
        res = -1
        l,r = 0, len(nums)-1
        # mid = (l + r) // 2

        # right pivot : 345612
            # (1) - know that 3-5 is sequential; 1 not inside; go R-->
            # (4) - know that 3-5 is sequential; 4 inside; go <--L
        # left  pivot: 612345

        while l <= r:
            m = (l+r)//2 # index of midpoint
            
            if nums[m] == target: # Base Case
                return m
            else:
                if nums[m] <= nums[r]: # Right side is in order
                    if nums[m] < target <= nums[r]:
                        l = m+ 1
                    else:
                        r = m-1
                else: # left side in order
                    if nums[l] <= target < nums[m]:
                        r = m-1
                    else:
                        l = m+1
        return res