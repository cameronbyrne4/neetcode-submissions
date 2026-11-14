class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = [] # global array for each subset
        nums.sort()
        def dfs(i): # i is the index of the value we are either accepting or denying
            # Gone past the leaf node, we are done deciding this subset
            if i >= len(nums):
                res.append(subset.copy()) # In py we use copy because subset gets modified
                return

            # Path 1: use the current one
            subset.append(nums[i])
            dfs(i+1) # make the decision on the next num
            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
            # Path 2: Don't use it! (If this is the 2nd in a row, CANCEL this path)
                i += 1

            dfs(i+1)
        
        dfs(0)
        return res