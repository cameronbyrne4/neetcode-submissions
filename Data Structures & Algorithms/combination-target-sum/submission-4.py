class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        doing all combos
        - last time it was either Y or N for each number
        - now we can add it however many times we want..
        - stop once we get above the target i present
        - options: add i, or any other number
        '''
        
        result = []
        subset = []
        
        def dfs(i, sum, t):
            
            print("sum is", sum)
            if sum > t or i > len(nums)-1: # stop if too big or end of nums
                return
            if sum == t:
                result.append(subset.copy()) # copy cuz we have one list
                return

            # if we aren't at target yet we add any of the numbers
            
            # Paht 1: can include it
            subset.append(nums[i])
            dfs(i,sum+nums[i], t)

            # paht 2:
            subset.pop()
            dfs(i+1, sum, t)

            
        dfs(0,0, target)
        return result

            # subset.pop()  NOTE: not including this I dont think since we won't add []