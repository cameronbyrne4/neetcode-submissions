class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for each number in the list, we can either add it or not!
        # 2^n decisions are made because each n is 2 paths to go down

        res = []
        subset = [] # global array for each subset

        def dfs(i): # i is the index of the value we are either accepting or denying
            # Gone past the leaf node, we are done deciding this subset
            if i >= len(nums):
                res.append(subset.copy()) # In py we use copy because subset gets modified
                return

            # Path 1: use the current one
            subset.append(nums[i])
            dfs(i+1) # make the decision on the next num

            # Path 2: Don't use it!
            subset.pop() # takes out the element at the END that we just added
            dfs(i+1)
        
        dfs(0)
        return res

        