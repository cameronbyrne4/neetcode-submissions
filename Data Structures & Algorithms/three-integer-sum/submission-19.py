class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort and do 3 pointers

        1. iterate over L skipping dupes
        2. at each L do 2 pointers

        A+B+C = 0
        -A = B+C
        '''

        res = []
        nums.sort()
        print(nums)
        for l in range(0,len(nums)-2):
            # Duplicate breaker
            if l>0 and nums[l] == nums[l-1]:
                continue

            # run 2 pointer
            m = l+1
            r = len(nums)-1
                # Target sum is -l (should be positive)
            
            while m < r:
                print("vars: ", l, m, r)
                # base case success
                if ((nums[m] + nums[r]) == -nums[l]):
                    print("W:",nums[l], nums[m], nums[r])
                    res.append([nums[l], nums[m], nums[r]])
                    # There can be multiple solution [-7,2,3,4,5]
                    # move both pointers inward with no does for m
                    m+= 1
                    while m > 0 and m < len(nums) and nums[m] == nums[m-1]:
                        m += 1
                    r -=1 
                elif ((nums[m] + nums[r]) > -nums[l]):
                    # Sum too big, r to left
                    r -= 1
                else:
                    m += 1
        return res
        